import pygame
from dialogue_box import DialogueBox
from dialogues.base import dialog_list
from game_object import GameObject
from base import width

def valid_pos(p, r):
    x, y = p
    return x >= r[0] and y <= r[1] and x <= r[2] and y >= r[3]

class Character(GameObject):
    def __init__(self, **kwargs):
        self.defaults = {"pos" : (0, 0),
                    "image" : None,
                    "name" : None,
                    "jump_height": 3,
                    "walk_dist": 2,
                    "rangec": [0, 0, 0, 0],
                    "color" : (255, 255, 255, 200),
                    "dir": 1
                    }
        super().parse_kwargs(kwargs, self.defaults)
        self.image = pygame.image.load(self.image)
        self.jumping = 0
        self.running = 0
        self.dialogue_index = 0
        self.dialogues = dialog_list.get(self.name, ["I do not have anything to say :("])
        self.talked = False

    def get_rect(self):
        rect = self.image.get_rect()
        rect.x, rect.y = self.pos
        return rect

    def show(self, screen):
        screen.blit(self.image, self.pos)

    def jump(self):
        if self.jumping == 0:
            self.jumping = 1
        x, y = self.pos
        y -= self.jump_height * self.jumping
        self.pos = (x, y)
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
        x, y = self.pos
        x += self.walk_dist * direction * (self.running + 1)
        if (valid_pos((x, y), self.rangec)):
            self.pos = (x, y)

    def talk(self, screen, character, chapter):
        chapter.special_event = True
        chapter.wait = True
        self.turn(-character.dir)
        if (chapter.dialogue_index) >= len(self.dialogues[chapter.time][int(self.talked)]):
            chapter.special_event = False
            chapter.dialogue_index = 0
            self.talked = True
            return (None, chapter)
        text = self.dialogues[chapter.time][int(self.talked)][int(not self.talked) * chapter.dialogue_index]
        chapter.dialogue_index += 1
        return (DialogueBox(text=text, color=self.color, rangec=(len(text) * 13, 40, min(self.get_rect().x - 40, width - len(text) * 15)  , self.get_rect().y - 70)), chapter)

    def collision(self, character):
        return self.get_rect().colliderect(character.get_rect())

