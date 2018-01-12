import pygame

class Drawer(object):
    def __init__(self, **kwargs):
        pass

    def graphic(self, screen, objects, background):
        screen.fill(0)
        screen.blit(background, (0, 0))
        for o in objects:
            if o:
                o.show(screen)
        pygame.display.flip()

    def school_graphic(self, screen, extra):
        from base import school_background
        from characters import kokichi, kaito
        self.graphic(screen, [kokichi, kaito] + extra, school_background)
