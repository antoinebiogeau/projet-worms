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
        self.jump()
        if self.constraints["isFalling"]:
            self.rect.y += 1 + self.velocity["y"]
        else:
            self.rect.y += self.velocity["y"]
        self.rect.x += 1 if self.actions["walk_right"] else -1 if  self.actions["walk_left"] else 0
        print(self.constraints["isFalling"])

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
        if Key().get_key_down(pygame.K_UP) and not self.actions["jump"] and not self.constraints["isFalling"]:
            self.actions["jump"] = True

    def jump(self):
        if self.actions["jump"]:
            self.velocity["y"] = -3
            self.time += 0.1
        if self.time > 5:
            self.velocity["y"] = 0
            self.actions["jump"] = False
        if self.constraints["isFalling"] == False:
            self.time = 0

