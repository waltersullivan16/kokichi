import pygame
from base import Movements, pos, screen, kokichi, background, keys, running, jump_height, max_height, min_height, event_dict, event_types, walk_dist, jumping, height, width, pos_others, kaito, Characters, font

def jump():
    global keys, pos, jumping
    if jumping == 0:
        jumping = 1
    x, y = pos
    y -= jump_height * jumping
    pos = (x, y)
    if (y <= max_height):
        jumping = -1
    if (y >= min_height):
        jumping = 0

def valid_pos(p):
    x, y = p
    return x > 0 and y > 0 and x < (width - 50) and y < height

def walk():
    global keys, pos
    x, y = pos
    x += (walk_dist * (keys[Movements.RIGHT.value] - keys[Movements.LEFT.value])) * (keys[Movements.RUN.value] + 1)
    if (valid_pos((x,y))):
        pos = (x, y)

def handle_keys():
    global keys, jumping
    if keys[Movements.JUMP.value] or keys[Movements.UP.value] or jumping != 0:
        jump()
    if keys[Movements.RIGHT.value] or keys[Movements.LEFT.value]:
        walk()
    if keys[Movements.ESCAPE.value]:
        pygame.quit()
        exit(0)

def set_kaito():
    global pos_others
    pos_others[Characters.KAITO.value] = (600, 230)

def collision(x, y, character):
    r1 = x.get_rect()
    r2 = y.get_rect()
    r1.x, r1.y = pos
    r2.x, r2.y = pos_others[character.value]
    print(r1, r2)
    return r1.colliderect(r2)

def talk(character):
    screen.blit(*make_prompt())
    pygame.display.flip()
    while 1:
        pass

def make_prompt():
    pygame.draw.rect(screen, pygame.Color("black"), (10, 320, 700, 50))
    message = 'Please type a color name for background (ex. "red"):'
    rend = font.render(message, True, pygame.Color("white"))
    return (rend, rend.get_rect(topleft=(20,330)))

def school_graphic():
    set_kaito()
    screen.fill(0)
    screen.blit(background, (0, 0))
    screen.blit(kokichi, pos)
    screen.blit(kaito, pos_others[Characters.KAITO.value])
    pygame.display.flip()

while running:
    global keys
    school_graphic()
    for event in pygame.event.get():
        if event.type in event_types:
            keys[event_dict.get(event.key, 'not_handled')] += (event.type == pygame.KEYDOWN) - (event.type == pygame.KEYUP)
    handle_keys()
    if collision(kokichi, kaito, Characters.KAITO):
        talk(Characters.KAITO)
