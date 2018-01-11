import pygame
from base import Movements, width, height, kokichi, running, event_dict, event_types, kaito, school_background
from drawing import graphic

keys = len(Movements) * [0]

def handle_keys():
    if keys[Movements.JUMP.value] or keys[Movements.UP.value] or kokichi.jumping != 0:
        kokichi.jump()
    kokichi.running = keys[Movements.RUN.value]
    if keys[Movements.RIGHT.value] or keys[Movements.LEFT.value]:
        kokichi.walk(keys[Movements.RIGHT.value] - keys[Movements.LEFT.value])
    if keys[Movements.ESCAPE.value]:
        pygame.quit()
        exit(0)

screen = pygame.display.set_mode((width, height))
while running:
    graphic(screen, [kokichi, kaito], school_background)
    for event in pygame.event.get():
        if event.type in event_types:
            keys[event_dict.get(event.key, 'not_handled')] += (event.type == pygame.KEYDOWN) - (event.type == pygame.KEYUP)
    handle_keys()
    if kokichi.collision(kaito):
        kaito.talk(screen, kokichi)
