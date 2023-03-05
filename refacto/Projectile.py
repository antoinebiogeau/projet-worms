import pygame
from wind import Wind

class Projectile:
    def __init__(self, position, velocity, type="GSF"):
        self.rect = pygame.Rect(position[0],position[1], 10,10)
        self.velocity = velocity
        self.time = 0
        self.type = type
        

    def update(self, screen):
        if type == "GSF":
            self.time += 0.005
            self.rect.x = self.velocity[0] * self.time + self.rect.x
            self.rect.y = 9.81/2 * self.time ** 2 + self.velocity[1] * self.time + self.rect.y
            pygame.draw.rect(screen, (255,0,0), self.rect)
        elif type == "GF":
            self.time += 0.005
            self.rect.x = self.velocity[0] * self.time + self.rect.x
            self.rect.y = 9.81/2 * self.time ** 2 + self.velocity[1] * self.time + self.rect.y
            pygame.draw.rect(screen, (255,0,0), self.rect)
        elif type == "RK":
            self.time += 0.005
            self.rect.x = self.velocity[0] * self.time + self.rect.x
            self.rect.y = 9.81/2 * self.time ** 2 + self.velocity[1] * self.time + self.rect.y
            pygame.draw.rect(screen, (255,0,0), self.rect)
        self.time += 0.1
        self.rect.x = self.velocity[0] * self.time + self.rect.x + Wind().getWind()[0]
        self.rect.y = 9.81/2 * self.time ** 2 + self.velocity[1] * self.time + self.rect.y + Wind().getWind()[1]
        pygame.draw.rect(screen, (255,0,0), self.rect)

    def collide(self, target, target_type=1):
       if target_type == 1:
            if self.rect.colliderect(target.rect):
                target.hp -= 50
                print("Projectile collide")
                return True
            return False
       elif self.rect.colliderect(target):
           return True
       return False
    
    def explode(self, screen):
        pygame.draw.circle(screen, (255,0,0), (self.rect.x, self.rect.y), 50)



    
        


