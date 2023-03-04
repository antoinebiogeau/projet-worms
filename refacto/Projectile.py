import pygame

class Projectile:
    def __init__(self, position):
        self.rect = pygame.Rect(position[0],position[1], 10,10)
        self.velocity = (-2,0)
        self.time = 0
        

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

    def collide(self, target):
       if self.rect.colliderect(target.rect):
           target.hp -= 50
           return True
       return False

    
        


