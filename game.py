import pygame
from base import width, height, running
from drawing import school_graphic
from keys_handler import event_handler


screen = pygame.display.set_mode((width, height))
while running:
    school_graphic(screen)
    event_handler(screen)
