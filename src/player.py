import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite): 
    def __init__(self, name, color, x, y):
        super().__init__() 
        self.name = name
        self.color = color #team
        self.x = x
        self.y = y
        self.life = 100
        self.isJumping = False
        self.isAlive = True
        self.isFalling = True
        self.collider = Rect(self.x, self.y, 32,32)
        self.rect = self.image.get_rect(topleft=(x, y))
        ##charger l'image du joueur
        self.image = pygame.image.load("../assets/character.png").convert_alpha()

    def jump(self):
        if not self.isJumping:
            self.isJumping = True
            self.jumpSpeed = 15
            self.jumpDuration = 0

    def update(self, dt, area, map):
        if self.isJumping:
            self.jumpDuration += dt
            if self.jumpDuration <= 500:
                self.rect.y -= self.jumpSpeed
                self.jumpSpeed -= 1
            else:
                self.isJumping = False
                self.isFalling = True
        
        if self.isFalling:
            self.rect.y += 10
            self.collide(map, area)


    def collide(self, map, area): 
        for i in range(self.rect.y, self.rect.y + self.rect.height):
            for j in range(self.rect.x, self.rect.x + self.rect.width):
                if area[j][i] == 1:
                    self.isFalling = False


    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.isAlive = False
            self.kill()
        else:
            self.healthBar.update(self.health)