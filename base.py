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

class Characters(Enum):
    KAITO = 0

pygame.init()
width, height = 729, 376
screen = pygame.display.set_mode((width, height))
pos = (20, 240)
keys = len(Movements) * [0]

kokichi = pygame.image.load("pics/kokichi.png")
kaito = pygame.image.load("pics/luminary_of_the_stars.png")
background = pygame.image.load("pics/hallway.png")
running = 1
jump_height = 3
max_height = 150
min_height = 240
walk_dist = 2

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
jumping = 0
pos_others = [(0,0)] * len(Characters)
font = pygame.font.SysFont("comicsansms", 20)
