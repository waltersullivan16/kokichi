import pygame
from base import Movements, screen, kokichi, background, keys, running, max_height, min_height, event_dict, event_types, height, width, kaito, Character, font



def handle_keys():
    global keys
    if keys[Movements.JUMP.value] or keys[Movements.UP.value] or kokichi.jumping != 0:
        kokichi.jump()
    kokichi.running = keys[Movements.RUN.value]
    if keys[Movements.RIGHT.value] or keys[Movements.LEFT.value]:
        kokichi.walk(keys[Movements.RIGHT.value] - keys[Movements.LEFT.value])
    if keys[Movements.ESCAPE.value]:
        pygame.quit()
        exit(0)

def collision(character1, character2):
    return character1.get_rect().colliderect(character2.get_rect())

def talk(character):
    text = "fdsfsa"
    make_prompt(text)
    pygame.display.flip()
    while 1:
        pass

def make_prompt(text):
    s = pygame.Surface(((width - 20), (height // 9)), pygame.SRCALPHA)
    s.fill((255,255,255,200))
    screen.blit(s, (10, ((15 * height) // 18)))
    screen.blit(font.render(text, True, pygame.Color("white")), (0,0))

def school_graphic():
    screen.fill(0)
    screen.blit(background, (0, 0))
    kokichi.show(screen)
    kaito.show(screen)
    pygame.display.flip()

while running:
    global keys
    school_graphic()
    for event in pygame.event.get():
        if event.type in event_types:
            keys[event_dict.get(event.key, 'not_handled')] += (event.type == pygame.KEYDOWN) - (event.type == pygame.KEYUP)
    handle_keys()
    if collision(kokichi, kaito):
        talk(kaito)
