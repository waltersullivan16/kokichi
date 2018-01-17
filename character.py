import pygame
from dialogue_box import DialogueBox
from dialogues.base import dialog_list
from base import width

class Character(pygame.sprite.Sprite):
    def __init__(self, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.image = pygame.image.load(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos
        self.dialogue_index = 0
        self.dialogues = dialog_list.get(self.name, ["I do not have anything to say :("])
        self.talked = False
        self.dir = 1

    def turn(self, direction):
        if self.dir != direction:
            self.image = pygame.transform.flip(self.image, True, False)
            self.dir = -self.dir

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
        return (DialogueBox(text=text, color=self.color, rangec=(len(text) * 13, 40, min(self.rect.x - 40, width - len(text) * 15)  , self.rect().y - 70)), chapter)

