import pygame
from base import Movements, width, height, kokichi, background, running, event_dict, event_types, kaito

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

def school_graphic():
    screen.fill(0)
    screen.blit(background, (0, 0))
    kokichi.show(screen)
    kaito.show(screen)
    pygame.display.flip()

screen = pygame.display.set_mode((width, height))
while running:
    school_graphic()
    for event in pygame.event.get():
        if event.type in event_types:
            keys[event_dict.get(event.key, 'not_handled')] += (event.type == pygame.KEYDOWN) - (event.type == pygame.KEYUP)
    handle_keys()
    if kokichi.collision(kaito):
        kaito.talk(screen)
