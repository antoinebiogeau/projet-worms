import pygame
import Constant
from key import Key

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hp = 100
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
        self.collider = {
            "mask": pygame.Mask((self.rect.width - 10, self.rect.height * 0.1)),
            "offset": (self.rect.x + 5, self.rect.y + self.rect.height * 0.9 + 2),
        }

    def update(self, screen):
        self.checkActions()
        self.jump()
        if self.constraints["isFalling"]:
            self.rect.y += 1 + self.velocity["y"]
        else:
            self.rect.y += self.velocity["y"]
        self.rect.x += 1 if self.actions["walk_right"] else -1 if  self.actions["walk_left"] else 0
        print(self.constraints["isFalling"])

        #draw UI
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, Constant.RED_TEAM, (self.rect.x, self.rect.y - 10, self.rect.width  * (self.hp / 100), 5))
        pygame.draw.rect(screen, (100,0,0), (self.rect.x, self.rect.y - 10, self.rect.width, 5), 1)

    def collide(self, object):
        pass

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
        if Key().get_key_down(pygame.K_SPACE):
            self.hp -= 0.1

    def jump(self):
        if self.actions["jump"]:
            self.velocity["y"] = -3
            self.time += 0.1
        if self.time > 5:
            self.velocity["y"] = 0
            self.actions["jump"] = False
        if self.constraints["isFalling"] == False:
            self.time = 0

    def drawColliders(self):
        pygame.draw.rect(self.collider["mask"].to_surface(setcolor=(0,255,0,255)), self.collider["offset"])