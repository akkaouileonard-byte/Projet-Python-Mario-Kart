from constants import CIRCUIT_GRID_1_COLOR,CIRCUIT_GRID_2_COLOR, GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile


class GameModel:

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None
        self.available_circuits = [CIRCUIT_GRID_1_COLOR, CIRCUIT_GRID_2_COLOR] # les autres circuits peuvent être ajoutés ici
        self.selected_circuit_index: int = 0

    def previous_circuit(self) -> None:
        total_circuits = len(self.available_circuits)
        self.selected_circuit_index = (self.selected_circuit_index - 1) % total_circuits

    def next_circuit(self) -> None:
        total_circuits = len(self.available_circuits) 
        self.selected_circuit_index = (self.selected_circuit_index + 1) % total_circuits

    def load_circuit(self) -> None:
        current_color = self.available_circuits[self.selected_circuit_index]
        selected_grid = [ [RoadTile(col=col_idx, row=row_idx, color=current_color) for col_idx in range(GRID_COLS)] for row_idx in range(GRID_ROWS) ]
        self.circuit = Circuit(grid=selected_grid)
        self.spawn_car()

    def spawn_car(self) -> None:
        self.car = Car(3, 3)

    def update(self) -> None:
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()
