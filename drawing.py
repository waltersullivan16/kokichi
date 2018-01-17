import pygame

class Drawer(object):
    def __init__(self, **kwargs):
        pass

    def graphic(self, screen, objects, background, all_sprites):
        screen.fill(0)
        screen.blit(background, (0, 0))
        for o in objects:
            if o:
                o.show(screen)
        all_sprites.draw(screen)
        pygame.display.flip()

    def school_graphic(self, screen, extra, all_sprites):
        from base import school_background
        self.graphic(screen, extra, school_background, all_sprites)
