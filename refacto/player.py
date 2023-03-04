import pygame
import Constant
from key import Key

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.actions = {
            "walk_left": False,
            "walk_right": False,
            "jump": False
        }
        self.velocity = {
            "x": 0,
            "y": 0
        }
        self.constraints = {
            "isFalling": True
        }
        self.image = pygame.image.load("assets/character.png")
        self.rect = self.image.get_rect()
        self.time = 0

    def update(self):
        self.checkActions()
        if self.constraints["isFalling"]:
            self.rect.y += 1 + self.velocity["y"]
        else:
            self.rect.y += self.velocity["y"]
        self.rect.x += 1 if self.actions["walk_right"] else -1 if  self.actions["walk_left"] else 0

    def collide(self, object):
        if self.rect.y + self.rect.height == object.y:
            self.constraints["isFalling"] = False
        else:
            self.constraints["isFalling"] = True

    def checkActions(self):
        if Key().get_key_down(pygame.K_RIGHT):
            self.actions["walk_right"] = True
        else:
            self.actions["walk_right"] = False
        if Key().get_key_down(pygame.K_LEFT):
            self.actions["walk_left"] = True
        else:
            self.actions["walk_left"] = False
        if Key().get_key_down(pygame.K_UP) and not self.constraints["isFalling"]:
            self.actions["jump"] = True

    def jump(self):
        if self.actions["jump"]:
            self.velocity["y"] = -2
            self.time += 0.5
        if self.time > 3:
            self.actions["jump"] = False
            self.time = 0
