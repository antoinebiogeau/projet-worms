import pygame

class Projectile:
    def __init__(self):
        self.rect = pygame.Rect(10,250, 10,10)
        self.velocity = (15,5)
        self.time = 0
        

    def update(self, screen):
        self.time += 0.005
        self.rect.x = self.velocity[0] * self.time + self.rect.x
        self.rect.y = 9.81/2 * self.time ** 2 + self.velocity[1] * self.time + self.rect.y
        pygame.draw.rect(screen, (255,0,0), self.rect)
        


