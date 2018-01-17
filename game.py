import pygame
from base import width, height, running
from drawing import Drawer
from keys_handler import event_handler
from chapter import Chapter
from platform import Platform
from characters import kokichi, kaito


screen = pygame.display.set_mode((width, height))
drawer = Drawer()
chapter = Chapter()
extra = []
all_sprites = pygame.sprite.Group()
all_sprites.add(Platform(100, 100, 100, 100))
all_sprites.add(kokichi)
all_sprites.add(kaito)
while running:
    drawer.school_graphic(screen, extra, all_sprites)
    extra = event_handler(screen, extra, chapter)
