import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill((149, 38, 171))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
