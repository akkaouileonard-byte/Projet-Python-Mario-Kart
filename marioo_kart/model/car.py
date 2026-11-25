import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE, CAR_MAX_REVERSE_SPEED
)

class Car:
    """
    Représente le kart sur le circuit et gère sa physique et son affichage.

    Attributes:
        x (float): Position horizontale du centre de la voiture en pixels.
        y (float): Position verticale du centre de la voiture en pixels.
        speed (float): Vitesse actuelle de déplacement de la voiture.
        angle (float): Orientation de la voiture en degrés (180.0 = vers le haut).
        sprite (pygame.Surface): Image de base de la voiture avec son marqueur avant.
    
    """
    def __init__(self, start_col: int, start_row: int):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 180.0
        self.sprite = self.build_sprite()

    def accelerate(self) -> None:
        self.speed += CAR_ACCELERATION
    
    def brake(self) -> None:
        self.speed += -CAR_ACCELERATION
        if self.speed < -CAR_MAX_REVERSE_SPEED:
            self.speed = -CAR_MAX_REVERSE_SPEED

    def update_position(self) -> None:
        """
        Met à jour les coordonnées (x, y) de la voiture selon sa vitesse et son angle."
        # Conversion de l'angle en radians pour les fonctions trigonométriques
        rad = math.radians(self.angle)

        Déplacement selon l'orientation du marqueur :
        - À 180° (haut) : sin(180°) = 0, cos(180°) = -1 -> y diminue (monte)
        - À 0° (bas)    : sin(0°) = 0,   cos(0°) = 1    -> y augmente (descend)
        - À 90° (gauche): sin(90°) = 1,  cos(90°) = 0   -> x diminue (va à gauche)

        """
        rad = math.radians(self.angle)
        self.x -= self.speed * math.sin(rad)
        self.y += self.speed * math.cos(rad)

    def build_sprite(self) -> pygame.Surface:
        """
        Génère la surface graphique de la voiture avec son marqueur avant.

        Returns:
            pygame.Surface: L'image de base de la voiture orientée vers le bas (angle 0°).

        """
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)

        # 1. Corps principal de la voiture (rouge)
        pygame.draw.rect(surf, (255, 0, 0), (0, 0, CAR_WIDTH, CAR_HEIGHT), border_radius=5)

        # 2. Marqueur à l'avant (pare-brise / capot plus clair en bas du sprite)
        front_height = int(CAR_HEIGHT * 0.25)  # 25 % de la longueur de la voiture
        margin = 4  # Marge sur les côtés pour un rendu propre

        pygame.draw.rect(
            surf,
            (255, 160, 160),  # Rouge clair 
            (margin, CAR_HEIGHT - front_height - 5, CAR_WIDTH - 2 * margin, front_height),
            border_radius=1
        )
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        """
        Pivote l'image de la voiture selon son angle actuel et recentre son rectangle.

        Returns:
            tuple[pygame.Surface, pygame.Rect]: Un tuple contenant la surface pivotée
            et son rectangle de positionnement centré sur (x, y).
        
        """
        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect


        
