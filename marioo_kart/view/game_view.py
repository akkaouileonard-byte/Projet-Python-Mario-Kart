import pygame
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, TILE_SIZE,
    COLOR_BG, COLOR_TEXT, COLOR_ACCENT, COLOR_PANEL, COLOR_PANEL_BORDER,
    GameState
)
from model.game_model import GameModel


class GameView:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, model: GameModel) -> None:
        self.screen.fill(COLOR_BG)
        if model.state == GameState.MENU:
            self._draw_menu(model)
        elif model.state == GameState.SELECT_CIRCUIT:
            self._draw_select_circuit(model)
        elif model.state == GameState.RACING:
            self._draw_racing(model)

    def _draw_menu(self, model: GameModel) -> None:
        cx = WINDOW_WIDTH // 2

        title_surf = self.font.render(
            "Jeu de course 2D", True, COLOR_ACCENT)
        self.screen.blit(title_surf, title_surf.get_rect(center=(cx, 160)))

        options = [("SELECTIONNEZ CIRCUIT (Enter)", GameState.SELECT_CIRCUIT),
                   ("QUITTER (Escape)", None)]
        for i, (label, _) in enumerate(options):
            y = 320 + i * 80
            rect = pygame.Rect(cx - 140, y - 25, 280, 50)
            pygame.draw.rect(self.screen, COLOR_PANEL, rect, border_radius=8)
            pygame.draw.rect(self.screen, COLOR_PANEL_BORDER,
                             rect, 2, border_radius=8)
            text_surf = self.font.render(
                label, True, COLOR_ACCENT if i == 0 else COLOR_TEXT)
            self.screen.blit(text_surf, text_surf.get_rect(center=rect.center))

    def _draw_select_circuit(self, model: GameModel) -> None:
        cx = WINDOW_WIDTH // 2
        title_surf = self.font.render("CHOISIR UN CIRCUIT", True, COLOR_ACCENT) 
        self.screen.blit(title_surf, title_surf.get_rect(center=(cx, 140)))
        circuit_names = ["Circuit 1 (Classic)", "Circuit 2 (Advance)"]
        for i, name in enumerate(circuit_names):
            y = 280 + i * 80 
            rect = pygame.Rect(cx - 160, y - 25, 320, 50)

            is_selected = (i == model.selected_circuit_index)  

            border_color = COLOR_ACCENT if is_selected else COLOR_PANEL_BORDER 
            text_color = COLOR_ACCENT if is_selected else COLOR_TEXT 
            border_width = 3 if is_selected else 1 

            pygame.draw.rect(self.screen, COLOR_PANEL, rect, border_radius=8)
            pygame.draw.rect(self.screen, border_color, rect, border_width, border_radius=8)
            
            display_text = f"> {name} <" if is_selected else name 
            text_surf = self.font.render(display_text, True, text_color)
            self.screen.blit(text_surf, text_surf.get_rect(center=rect.center))
            
        help_surf = self.font.render("Up/Down: Choisir | Enter: Jouer | ESC: Retour", True, COLOR_TEXT)
        self.screen.blit(help_surf, help_surf.get_rect(center=(cx, 550)))

    def _draw_racing(self, model: GameModel) -> None:

        for row_idx, row in enumerate(model.circuit.grid):
            for col_idx, tile in enumerate(row):
                sprite = tile.get_sprite(TILE_SIZE)
                self.screen.blit(
                    sprite, (col_idx * TILE_SIZE, row_idx * TILE_SIZE))

        if model.circuit is None:
            return
        surf, rect = model.car.get_rotated_sprite()
        self.screen.blit(surf, rect)
