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
def valid_pos(p):
    x, y = p
    return x > 0 and y > 0 and x < (width - 50) and y < height

class Character(object):
    def __init__(self, **kwargs):
        self.parse_kwargs(kwargs)
        self.image = pygame.image.load(self.image)
        self.jumping = 0
        self.running = 0

    def parse_kwargs(self, kwargs):
        defaults = {"pos" : (0, 0),
                    "image" : None,
                    "name" : None,
                    "jump_height": 3,
                    "walk_dist": 2,
                    }
        for kwarg in kwargs:
            if kwarg in defaults:
                defaults[kwarg] = kwargs[kwarg]
            else:
                raise KeyError("Character accepts no keyword {}.".format(kwarg))
        self.__dict__.update(defaults)

    def get_rect(self):
        rect = self.image.get_rect()
        rect.x, rect.y = self.pos
        return rect

    def show(self, screen):
        screen.blit(self.image, self.pos)

    def jump(self):
        if self.jumping == 0:
            self.jumping = 1
        x, y = self.pos
        y -= self.jump_height * self.jumping
        self.pos = (x, y)
        if (y <= max_height):
            self.jumping = -1
        if (y >= min_height):
            self.jumping = 0

    def walk(self, direction):
        x, y = self.pos
        x += self.walk_dist * direction * (self.running + 1)
        if (valid_pos(self.pos)):
            self.pos = (x, y)



pygame.init()
width, height = 729, 376
screen = pygame.display.set_mode((width, height))
keys = len(Movements) * [0]

running = 1
kokichi = Character(pos=(20, 240), image="pics/kokichi.png",name="Kokichi")
kaito = Character(pos=(600, 230), image="pics/luminary_of_the_stars.png", name="Kaito")
background = pygame.image.load("pics/hallway.png")
max_height = 150
min_height = 240

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
font = pygame.font.SysFont("comicsansms", 20)
