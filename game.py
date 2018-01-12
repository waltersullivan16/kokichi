import pygame
from base import width, height, running
from drawing import Drawer
from keys_handler import event_handler
from chapter import Chapter


screen = pygame.display.set_mode((width, height))
drawer = Drawer()
chapter = Chapter()
extra = []
while running:
    drawer.school_graphic(screen, extra)
    extra = event_handler(screen, extra, chapter)
