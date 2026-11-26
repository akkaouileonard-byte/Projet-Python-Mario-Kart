from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile, HerbeTile, TerreTile, GlaceTile, VideTile 

LAYOUT_MALICK_1 = [ "TTTRRRTTTRRRGGGG",
                    "TTRRTRRTTTRTGGGG",
                    "TRRRTTRRRTRVGGGG",
                    "RRRVVVVVRRRVGVHH",
                    "RRRGGGGVRRRVGRHH",
                    "RRRVVVGVTTTVGRHH",
                    "RRRTTVGVVVVVGVHH",
                    "RRRRTVGGGGGGGVHH",
                    "RRTRRVVVVVVVVVHH",
                    "RRRRRRRRHHHHHHHH",
                    "RRRRRRRRHHHHHHHH",
                    "RRRRRRRRHHHHHHHH", ] 

LAYOUT_CLASSIC_2 = [ "RRRRRRRRRRRRRRRR",
                     "RHHHHHHHHHHHHHHR",
                     "RHHHHHHHHHHHHHHR",
                     "RHHHRRRRRRRRHHHR",
                     "RHHHRHHHHHHRHHHR",
                     "RHHHRHHHHHHRHHHR",
                     "RHHHRHHHHHHRHHHR",
                     "RHHHRRRRRRRRHHHR", 
                     "RHHHHHHHHHHHHHHR",
                     "RHHHHHHHHHHHHHHR",
                     "RRRRRRRRRRRRRRRR",
                     "RRRRRRRRRRRRRRRR", ]

class GameModel:
    """
    Gère l'état global, la logique et les entités principales du jeu.

    Attributes:
        state (str): État actuel du jeu (ex. : menu, course en cours).
        circuit (Circuit | None): Instance du circuit chargé, ou None avant le chargement.
        car (Car | None): Instance de la voiture du joueur, ou None avant son apparition.
    
    """
    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None
        self.available_circuits = [LAYOUT_MALICK_1, LAYOUT_CLASSIC_2] # les autres circuits peuvent être ajoutés ici
        self.selected_circuit_index: int = 0

    def previous_circuit(self) -> None:
        self.selected_circuit_index = (self.selected_circuit_index - 1) % len(self.available_circuits)

    def next_circuit(self) -> None:
        self.selected_circuit_index = (self.selected_circuit_index + 1) % len(self.available_circuits)

    def load_circuit(self) -> None:

        selected_layout = self.available_circuits[self.selected_circuit_index] 

        tile_mapping = { "R": RoadTile, 
                         "H": HerbeTile,
                         "T": TerreTile,
                         "G": GlaceTile,
                         "V": VideTile, }
        
        grid = [
            [
                tile_mapping[selected_layout[row_idx][col_idx]](col=col_idx, row=row_idx) 
                for col_idx in range(GRID_COLS)
            ] 
            for row_idx in range(GRID_ROWS)
        ]
        
        self.circuit = Circuit(grid=grid) 
        self.spawn_car()

    def spawn_car(self) -> None:
    # Crée et place la voiture sur sa case de départ en bas à gauche du circuit.
        self.car = Car(0, 11)

    def update(self) -> None:
    # Met à jour la simulation du jeu à chaque image lorsque la course est active.
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()
