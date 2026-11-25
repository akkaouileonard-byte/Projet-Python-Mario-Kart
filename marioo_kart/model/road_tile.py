import pygame
from constants import TILE_SIZE


class RoadTile:

    def __init__(self, col: int, row: int, color: tuple[int, int, int] = (80, 80, 90)):
        self.col = col
        self.row = row
        self.color = color
        self.sprite: pygame.Surface | None = None

    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:
        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite
        surface = pygame.Surface((tile_size, tile_size))
        surface.fill(self.color)
        pygame.draw.rect(surface, (60, 60, 70), surface.get_rect(), 2)

        self.sprite = surface
        return self.sprite

class TerreTile:
    """
    classe représentant un terrain de terre (j'ai repris le patron RoadTile pour faire les autres)
    """

    def __init__(self, col: int, row: int):
            self.col = col
            self.row = row
            self.sprite: pygame.Surface | None = None
    
    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:
        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite
        surface = pygame.Surface((tile_size, tile_size))
        surface.fill((139, 90, 43))   # Marron terre
        pygame.draw.rect(surface, (110, 70, 30), surface.get_rect(), 2) # Bordure marron foncé
    
        self.sprite = surface
        return self.sprite

class HerbeTile:
    """
    classe représentant un terrain d'herbe (j'ai repris le patron RoadTile pour faire les autres)
    """

    def __init__(self, col: int, row: int):
            self.col = col
            self.row = row
            self.sprite: pygame.Surface | None = None
    
    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:
        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite
        surface = pygame.Surface((tile_size, tile_size))
        surface.fill((50, 160, 60)) # code RGB vert herbe
        pygame.draw.rect(surface, (40, 130, 50), surface.get_rect(), 2)  # bordure vert foncé
    
        self.sprite = surface
        return self.sprite

class GlaceTile:
    """
    classe représentant un terrain de glace (j'ai repris le patron RoadTile pour faire les autres)
    """

    def __init__(self, col: int, row: int):
            self.col = col
            self.row = row
            self.sprite: pygame.Surface | None = None
    
    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:
        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite
        surface = pygame.Surface((tile_size, tile_size))
        surface.fill((175, 238, 238))   # bleu glacier clair 
        pygame.draw.rect(surface, (130, 210, 225), surface.get_rect(), 2)   # Bordure bleu givre
    
        self.sprite = surface
        return self.sprite

class VideTile:
    """
    classe représentant un terrain de vide (j'ai repris le patron RoadTile pour faire les autres)
    """

    def __init__(self, col: int, row: int):
            self.col = col
            self.row = row
            self.sprite: pygame.Surface | None = None
    
    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:
        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite
        surface = pygame.Surface((tile_size, tile_size))
        surface.fill((15, 15, 20))   # Noir / abîme
        pygame.draw.rect(surface, (30, 30, 40), surface.get_rect(), 2)  # Bordure gris très sombre
    
        self.sprite = surface
        return self.sprite