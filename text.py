import pygame
from game_object import GameObject

class Text(GameObject):
    def __init__(self, **kwargs):
        self.defaults = {"color" : pygame.Color("black"),
                    "position": (0, 0),
                    "text": "",
                    "font": pygame.font.SysFont("comicsansms", 20)
                    }
        super().parse_kwargs(kwargs, self.defaults)

    def show(self, screen):
        screen.blit(self.font.render(self.text, True, self.color), self.position)

