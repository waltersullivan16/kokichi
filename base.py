import pygame
from enum import Enum
from pygame.locals import K_UP, K_w, K_a, K_s, K_d, K_ESCAPE, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_LSHIFT

class Movements(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    JUMP = 4
    FALL = 5
    RUN = 6
    ESCAPE = 7

pygame.init()
width, height = 729, 376

max_height = 150
min_height = 240
running = 1
school_background = pygame.image.load("resources/pics/hallway.png")

event_dict = dict([
        (K_UP, Movements.UP.value),
        (K_w, Movements.UP.value),
        (K_DOWN, Movements.DOWN.value),
        (K_s, Movements.DOWN.value),
        (K_RIGHT, Movements.RIGHT.value),
        (K_d, Movements.RIGHT.value),
        (K_LEFT, Movements.LEFT.value),
        (K_a, Movements.LEFT.value),
        (K_SPACE, Movements.JUMP.value),
        (K_ESCAPE, Movements.ESCAPE.value),
        (K_LSHIFT, Movements.RUN.value)
        ])
event_types = [pygame.KEYUP, pygame.KEYDOWN]

