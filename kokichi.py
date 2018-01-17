import pygame

def valid_pos(p, r):
    x, y = p
    return x >= r[0] and y <= r[1] and x <= r[2] and y >= r[3]

class Kokichi(pygame.sprite.Sprite):
    def __init__(self, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.image = pygame.image.load("resources/pics/kokichi.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos
        self.jumping = 0
        self.running = 0
        self.name = "Kokichi"
        self.jump_height = 3
        self.walk_dist = 2
        self.dir = 1

    def jump(self):
        if self.jumping == 0:
            self.jumping = 1
        x, y = self.rect.x, self.rect.y
        y -= self.jump_height * self.jumping
        self.rect.x, self.rect.y = (x, y)
        if (y <= self.rangec[3]):
            self.jumping = -1
        if (y >= self.rangec[1]):
            self.jumping = 0

    def turn(self, direction):
        if self.dir != direction:
            self.image = pygame.transform.flip(self.image, True, False)
            self.dir = -self.dir

    def walk(self, direction):
        self.turn(direction)
        x, y = self.rect.x, self.rect.y
        x += self.walk_dist * direction * (self.running + 1)
        if (valid_pos((x, y), self.rangec)):
            self.rect.x, self.rect.y = (x, y)
