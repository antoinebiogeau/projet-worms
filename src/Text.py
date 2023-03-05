import pygame

class Text:
    instance = None

    def __init__(self):
        self.font = pygame.font.Font(None, 16)
        self.bigFont = pygame.font.Font(None, 32)

    def __call__(self, *args, **kwds):
        if instance is None:
            instance = super().__new__(self)
        return instance
    
    def render(self, screen,text, position, color, antialiasing=True, bigFont = False):
        if bigFont:
            textObj = self.bigFont.render(text,antialiasing, color)
        else:
            textObj = self.font.render(text,antialiasing, color)
        screen.blit(textObj, position)

