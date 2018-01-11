import pygame
from base import Movements, event_types, event_dict
from characters import kokichi, kaito

keys = len(Movements) * [0]

def clean_keys():
    for i in range(len(keys)):
        keys[i] = 0

def event_handler(screen):
    for event in pygame.event.get():
        if event.type in event_types:
            print(keys)
            print(event.key)
            key = event_dict.get(event.key, 'not_handled')
            keys[key] = int(event.type == pygame.KEYDOWN)
    handle_keys()
    if kokichi.collision(kaito):
        clean_keys()
        kaito.talk(screen, kokichi)

def handle_keys():
    if keys[Movements.JUMP.value] or keys[Movements.UP.value] or kokichi.jumping != 0:
        kokichi.jump()
    kokichi.running = keys[Movements.RUN.value]
    if keys[Movements.RIGHT.value] or keys[Movements.LEFT.value]:
        kokichi.walk(keys[Movements.RIGHT.value] - keys[Movements.LEFT.value])
    if keys[Movements.ESCAPE.value]:
        pygame.quit()
        exit(0)
