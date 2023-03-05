import pygame
from wind import Wind

class Projectile:
    def __init__(self, position, velocity, type):
        self.rect = pygame.Rect(position[0],position[1], 10,10)
        self.velocity = velocity
        self.time = 0
        self.type = type
        self.is_exploding = False
        self.gravity = 9.81
        self.timeBeforeExplode = 0
        self.timeAfterExplode = 0



    #rocket = high init speed, explode at impact 

    def update(self, screen):
        if self.type == 0:
            self.time += 0.1
            self.timeBeforeExplode += 0.1
            self.rect.x = (self.velocity[0] * 2) * self.time + self.rect.x + Wind().getWind()[0] * 0.5
            self.rect.y = self.gravity/2 * self.time ** 2 + (self.velocity[1] * 2) * self.time + self.rect.y + Wind().getWind()[1] * 0.5
        elif self.type == 1 and not self.is_exploding:
            self.time += 0.1
            self.timeBeforeExplode += 0.1
            self.rect.x = self.velocity[0] * self.time + self.rect.x
            self.rect.y = self.gravity/2 * self.time ** 2 + self.velocity[1] * self.time + self.rect.y
            if self.timeBeforeExplode > 10:
                self.is_exploding = True
        elif self.type == 2 and not self.is_exploding:
            self.time += 0.1
            self.timeBeforeExplode += 0.1
            self.rect.x = self.velocity[0] * self.time + self.rect.x + Wind().getWind()[0] * 0.5
            self.rect.y = self.gravity/2 * self.time ** 2 + self.velocity[1] * self.time + self.rect.y + Wind().getWind()[1] * 0.5
            if self.timeBeforeExplode > 10:
                self.is_exploding = True
        pygame.draw.rect(screen, (255,0,0), self.rect)
        

    def collide(self, target, target_type=1):
        if target_type == 1:
            if self.rect.colliderect(target.rect):
                self.is_exploding = True
        else: 
            if self.rect.colliderect(target):
                self.gravity = 0
                self.time = 0
                if self.type == 0:
                    self.velocity = (0,0)
                    self.is_exploding = True
                else:
                    self.velocity = (self.velocity[0] * 0.5, self.velocity[1] * .5)
            else:
                if self.type == 1 or self.type == 2:
                    self.gravity = 9.81
                    
                    
    
    def explode(self, screen, targets):
        if self.is_exploding:
            explosion = pygame.draw.circle(screen, (255,0,0), (self.rect.x, self.rect.y), 25)
            for target in targets:
                if target.rect.colliderect(explosion):
                    distance_x = explosion.centerx - target.rect.centerx
                    distance_y = explosion.centery - target.rect.centery
                    distance = distance_x ** 2 + distance_y ** 2
                    target.hp -= distance * 0.02
            self.timeAfterExplode += 0.1
            if self.timeAfterExplode > 2:
                return True
            else:
                return False
        
            



    
        


