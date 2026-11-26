import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE, CAR_ROTATION_SPEED, CAR_BRAKE, CAR_MAX_SPEED
)


class Car:

    def __init__(self, start_col: int, start_row: int):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.sprite = self.build_sprite()

    def accelerate(self) -> None:
        self.speed += CAR_ACCELERATION
        if self.speed > CAR_MAX_SPEED:
            self.speed = CAR_MAX_SPEED

    def brake(self) -> None:
        self.speed -= CAR_BRAKE
        if self.speed < 0:
            self.speed = 0
        

    def turn_left(self) -> None:
        if self.speed > 0:  # autoriser la voiture à tourner seulement si elle avance
            self.angle -= CAR_ROTATION_SPEED

    def turn_right(self) -> None:
        if self.speed > 0:  #pareil
            self.angle += CAR_ROTATION_SPEED

    def backward(self) -> None:
        self.speed -= CAR_ACCELERATION
        if self.speed < -CAR_MAX_SPEED / 2:
            self.speed = -CAR_MAX_SPEED / 2 #vitesse marche arrière max

    def update_position(self):
        angle_rad = math.radians(self.angle) #conversion de l'angle en radians

        self.x -= self.speed * math.sin(angle_rad)
        self.y += self.speed * math.cos(angle_rad)

    def build_sprite(self) -> pygame.Surface:
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 0, 0), (0, 0, CAR_WIDTH,
                         CAR_HEIGHT), border_radius=5)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect
