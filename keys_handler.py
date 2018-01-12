import pygame
from base import Movements, event_types, event_dict
from characters import kokichi, kaito
from text import TriviaText

keys = len(Movements) * [0]

def clean_keys():
    for i in range(len(keys)):
        keys[i] = 0

def event_handler(screen, extra, chapter):
    for event in pygame.event.get():
        if event.type in event_types:
            kokichi.wait = False
            key = event_dict.get(event.key, 'not_handled')
            keys[key] = int(event.type == pygame.KEYDOWN)
    return handle_keys(screen, extra, chapter)


def handle_keys(screen, extra, chapter):
    if kokichi.collision(kaito):
        if chapter.special_event or keys[Movements.JUMP.value]:
            if keys[Movements.JUMP.value] and not kokichi.wait:
                kaito.dialogue_index += 1
                kokichi.wait = True
                dialog, chapter = kaito.talk(screen, kokichi, chapter)
                return [dialog]
            return extra
        extra = [TriviaText(text="To talk press SPACE")]
    else:
        extra = []
    if keys[Movements.JUMP.value] or keys[Movements.UP.value] or kokichi.jumping != 0:
        kokichi.jump()
    kokichi.running = keys[Movements.RUN.value]
    if keys[Movements.RIGHT.value] or keys[Movements.LEFT.value]:
        kokichi.walk(keys[Movements.RIGHT.value] - keys[Movements.LEFT.value])
    if keys[Movements.ESCAPE.value]:
        pygame.quit()
        exit(0)
    return extra
