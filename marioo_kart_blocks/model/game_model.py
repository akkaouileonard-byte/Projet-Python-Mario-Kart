from constants import GameState, GRID_ROWS, GRID_COLS, TILE_SIZE, CAR_MAX_SPEED
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile
from model.blocks import StartBlock, CheckpointBlock, BoostBlock, FinishBlock
from model.course_manager import CourseManager


class GameModel:

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None
        self.race: CourseManager | None = None
        self.previous_tile = None

    def load_circuit(self) -> None:
        grid = [[RoadTile(col=col_idx, row=row_idx)
                for col_idx in range(GRID_COLS)] for row_idx in range(GRID_ROWS)]

        # Cases de test : elles pourront être déplacées sur le vrai circuit.
        grid[1][7].block = StartBlock(1)
        grid[4][7].block = CheckpointBlock(1)
        grid[6][7].block = BoostBlock(1.5)
        grid[8][7].block = CheckpointBlock(2)
        grid[10][7].block = FinishBlock()

        self.circuit = Circuit(grid=grid)
        self.race = CourseManager(total_laps=2, checkpoint_count=2)
        self.race.add_player(1, 7, 1)
        self.previous_tile = None
        self.spawn_car()

    def spawn_car(self) -> None:
        self.car = Car(7, 1)

    def update(self) -> None:
        if self.state != GameState.RACING or self.circuit is None:
            return
        if self.race.winner is not None:
            return

        self.car.update_position()
        tile = self.circuit.get_tile_at_pixel(self.car.x, self.car.y)

        # Une sortie de la grille est considérée comme du vide.
        if tile is None:
            self.respawn_car()
            return

        current_tile = (tile.col, tile.row)
        if current_tile != self.previous_tile:
            self.previous_tile = current_tile
            self.handle_block(tile, 1)

    def handle_block(self, tile, player_id):
        """Déclenche l'effet d'un bloc quand la voiture entre sur sa case."""
        block = tile.block

        if isinstance(block, CheckpointBlock):
            self.race.reach_checkpoint(
                player_id, block.checkpoint_id, tile.col, tile.row)
            print("Checkpoint", block.checkpoint_id, "validé")

        elif isinstance(block, BoostBlock):
            # Effet simple en attendant la physique définitive des voitures.
            self.car.speed = min(self.car.speed + block.boost_value,
                                 CAR_MAX_SPEED)
            print("BOOST !")

        elif isinstance(block, FinishBlock):
            if self.race.cross_finish(player_id):
                print("Tour validé :", self.race.laps[player_id])
                if self.race.winner is not None:
                    print("Victoire du joueur", self.race.winner)
            else:
                print("Checkpoints manquants !")

    def respawn_car(self, player_id=1):
        """Replace la voiture au dernier checkpoint après une sortie de carte."""
        col, row = self.race.get_respawn_position(player_id)
        self.car.x = col * TILE_SIZE + TILE_SIZE // 2
        self.car.y = row * TILE_SIZE + TILE_SIZE // 2
        self.car.speed = 0
        self.previous_tile = (col, row)
