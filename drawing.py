import pygame

def graphic(screen, characters, background):
    screen.fill(0)
    screen.blit(background, (0, 0))
    for character in characters:
        character.show(screen)
    pygame.display.flip()

def school_graphic(screen):
    from base import school_background
    from characters import kokichi, kaito
    graphic(screen, [kokichi, kaito], school_background)
