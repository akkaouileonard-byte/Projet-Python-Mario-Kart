import pygame
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, TILE_SIZE,
    COLOR_BG, COLOR_TEXT, COLOR_ACCENT, COLOR_PANEL, COLOR_PANEL_BORDER,
    GameState
)
from model.game_model import GameModel
from model.blocks import StartBlock, CheckpointBlock, BoostBlock, FinishBlock


class GameView:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, model: GameModel) -> None:
        self.screen.fill(COLOR_BG)
        if model.state == GameState.MENU:
            self._draw_menu(model)
        elif model.state == GameState.RACING:
            self._draw_racing(model)
        pygame.display.flip()

    def _draw_menu(self, model: GameModel) -> None:
        cx = WINDOW_WIDTH // 2

        title_surf = self.font.render(
            "Jeu de course 2D", True, COLOR_ACCENT)
        self.screen.blit(title_surf, title_surf.get_rect(center=(cx, 160)))

        options = [("JOUER (Enter)", GameState.RACING),
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

    def _draw_racing(self, model: GameModel) -> None:

        for row_idx, row in enumerate(model.circuit.grid):
            for col_idx, tile in enumerate(row):
                sprite = tile.get_sprite(TILE_SIZE)
                self.screen.blit(
                    sprite, (col_idx * TILE_SIZE, row_idx * TILE_SIZE))
                self.draw_block(tile)

        if model.circuit is None:
            return
        surf, rect = model.car.get_rotated_sprite()
        self.screen.blit(surf, rect)
        self.draw_race_info(model)

    def draw_block(self, tile) -> None:
        """Dessine une étiquette sur les cases qui contiennent un bloc."""
        block = tile.block
        if isinstance(block, StartBlock):
            color, label = (120, 120, 180), str(block.player_id)
        elif isinstance(block, CheckpointBlock):
            color, label = (50, 120, 220), "C" + str(block.checkpoint_id)
        elif isinstance(block, BoostBlock):
            color, label = (40, 180, 70), "B"
        elif isinstance(block, FinishBlock):
            color, label = (230, 160, 40), "F"
        else:
            return

        rect = pygame.Rect(tile.col * TILE_SIZE + 5,
                           tile.row * TILE_SIZE + 5,
                           TILE_SIZE - 10, TILE_SIZE - 10)
        pygame.draw.rect(self.screen, color, rect, border_radius=5)
        text = self.font.render(label, True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(center=rect.center))

    def draw_race_info(self, model: GameModel) -> None:
        """Affiche les tours, checkpoints et éventuellement le vainqueur."""
        if model.race is None:
            return

        race = model.race
        info = (f"Joueur 1 - Tours : {race.laps[1]}/{race.total_laps}"
                f" - Checkpoints : {len(race.checkpoints[1])}/{race.checkpoint_count}")
        pygame.draw.rect(self.screen, COLOR_PANEL, (0, 0, 590, 35))
        text = self.font.render(info, True, COLOR_TEXT)
        self.screen.blit(text, (10, 5))

        if race.winner is not None:
            message = self.font.render(
                f"JOUEUR {race.winner} GAGNANT !", True, COLOR_ACCENT)
            self.screen.blit(message, message.get_rect(
                center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)))
