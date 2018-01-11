import pygame
from text import Text
from game_object import GameObject

class DialogueBox(GameObject):
    def __init__(self, **kwargs):
        self.defaults = {
                "color" : (255, 255, 255),
                "alpha": 200,
                "rangec": [700, 40, 20, 310],
                "text": None
            }
        super().parse_kwargs(kwargs, self.defaults)

    def show(self, screen):
        rounded_rectangle = RoundedRect(
                rect=pygame.Rect((self.rangec[2],self.rangec[3],self.rangec[0],self.rangec[1])),
                color=pygame.Color(*self.color),
                alpha=self.alpha)
        screen.blit(rounded_rectangle.rectangle, (self.rangec[2], self.rangec[3]))
        Text(text=self.text, position=(self.rangec[2] + 10, self.rangec[3])).show(screen)
        pygame.display.flip()

class RoundedRect(GameObject):
    def __init__(self, **kwargs):
        self.defaults = {
                "rect": None,
                "radius": 0.4,
                "color": None,
                "alpha": 0,
            }
        super().parse_kwargs(kwargs, self.defaults)

        self.color.a      = 0
        self.rect.topleft = 0,0

        self.rectangle = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        circle = pygame.Surface([min(self.rect.size)*3]*2,pygame.SRCALPHA)
        pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
        circle = pygame.transform.smoothscale(circle,[int(min(self.rect.size)*self.radius)]*2)

        self.radius              = self.rectangle.blit(circle,(0,0))
        self.radius.bottomright  = self.rect.bottomright
        self.rectangle.blit(circle,self.radius)
        self.radius.topright     = self.rect.topright
        self.rectangle.blit(circle,self.radius)
        self.radius.bottomleft   = self.rect.bottomleft
        self.rectangle.blit(circle,self.radius)

        self.rectangle.fill((0,0,0),self.rect.inflate(-self.radius.w,0))
        self.rectangle.fill((0,0,0),self.rect.inflate(0,-self.radius.h))
        self.rectangle.fill(self.color,special_flags=pygame.BLEND_RGBA_MAX)
        self.rectangle.fill((255,255,255,self.alpha),special_flags=pygame.BLEND_RGBA_MIN)
