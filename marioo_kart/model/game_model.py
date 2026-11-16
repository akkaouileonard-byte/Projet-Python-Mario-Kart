from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile, HerbeTile, TerreTile, GlaceTile, VideTile


class GameModel:

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None

    def load_circuit(self) -> None:
        # Plan du circuit : 12 lignes (haut -> bas) de 16 colonnes (gauche -> droite)
        # V = Vide, H = Herbe, R = Route, T = Terre, G = Glace
        layout = [
            "VVHHHHHHHHHHHHVV",  # Ligne 0
            "VHRRRRRRRRRRRRHV",  # Ligne 1 
            "HRRHHHHHHHHHHRRH",  # Ligne 2
            "HRHHVVVVVVVVHHRH",  # Ligne 3
            "HTHHVVVVVVVVHHGH",  # Ligne 4 
            "HTHHVVHHHHVVHHGH",  # Ligne 5
            "HTHHVVHRRHVVHHGH",  # Ligne 6
            "HRHHHHHRRHHHHHRH",  # Ligne 7
            "HRRRRRRRHRRRRRRH",  # Ligne 8 
            "VHRRRRRRRRRRRRHV",  # Ligne 9
            "VVHHHHHHHHHHHHVV",  # Ligne 10
            "VVVVVVVVVVVVVVVV",  # Ligne 11
        ]

        # Dictionnaire de correspondance entre les lettres et tes classes
        tile_mapping = {
            "R": RoadTile,
            "H": HerbeTile,
            "T": TerreTile,
            "G": GlaceTile,
            "V": VideTile,
        }
        # Construction de la grille au format grille[row][col] (16 colonnes x 12 lignes) en m'aidant du code de départ :grid = [[RoadTile(col=col_idx, row=row_idx) for row_idx in range(GRID_COLS)] for col_idx in range(GRID_ROWS)]
        grid = [
            [
                tile_mapping[layout[row_idx][col_idx]](col=col_idx, row=row_idx)
                for col_idx in range(GRID_COLS)
            ]
            for row_idx in range(GRID_ROWS)
        ]

        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    def spawn_car(self) -> None:
        self.car = Car(7, 1)

    def update(self) -> None:
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()
