from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile, HerbeTile, TerreTile, GlaceTile, VideTile


class GameModel:
    """Gère l'état global, la logique et les entités principales du jeu.

    Attributes:
        state (str): État actuel du jeu (ex. : menu, course en cours).
        circuit (Circuit | None): Instance du circuit chargé, ou None avant le chargement.
        car (Car | None): Instance de la voiture du joueur, ou None avant son apparition.
    """

    def __init__(self):
        """Initialise le modèle du jeu dans l'état menu sans circuit ni voiture actifs."""
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None

    def load_circuit(self) -> None:
        """Construit la grille du circuit à partir du plan et fait apparaître la voiture."""
        # Plan du circuit : 12 lignes (haut -> bas) de 16 colonnes (gauche -> droite)
        # V = Vide, H = Herbe, R = Route, T = Terre, G = Glace
        layout = [
            "TTTRRRTTTRRRGGGG",  # Ligne 0
            "TTRRTRRTTTRTGGGG",  # Ligne 1
            "TRRRTTRRRTRVGGGG",  # Ligne 2
            "RRRVVVVVRRRVGVHH",  # Ligne 3
            "RRRGGGGVRRRVGRHH",  # Ligne 4
            "RRRVVVGVTTTVGRHH",  # Ligne 5
            "RRRTTVGVVVVVGVHH",  # Ligne 6
            "RRRRTVGGGGGGGVHH",  # Ligne 7
            "RRTRRVVVVVVVVVHH",  # Ligne 8
            "RRRRRRRRHHHHHHHH",  # Ligne 9
            "RRRRRRRRHHHHHHHH",  # Ligne 10
            "RRRRRRRRHHHHHHHH",  # Ligne 11
        ]

        # Dictionnaire de correspondance entre les lettres et les classes de tuiles
        tile_mapping = {
            "R": RoadTile,
            "H": HerbeTile,
            "T": TerreTile,
            "G": GlaceTile,
            "V": VideTile,
        }

        # Construction de la grille au format grid[row][col] (12 lignes x 16 colonnes) en m'aidant du code de départ :grid = [[RoadTile(col=col_idx, row=row_idx) for row_idx in range(GRID_COLS)] for col_idx in range(GRID_ROWS)]
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
        """Crée et place la voiture sur sa case de départ en bas à gauche du circuit."""
        self.car = Car(0, 11)

    def update(self) -> None:
        """Met à jour la simulation du jeu à chaque image lorsque la course est active."""
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()