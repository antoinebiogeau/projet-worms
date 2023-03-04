import math

import pygame


class weapon(pygame.sprite.Sprite):
    def __init__(self, direction, speed, owner, angle, x, y):
        super().__init__()
        self.direction = direction
        self.speed = speed
        self.owner = owner
        self.angle = angle
        self.x = x
        self.y = y
        self.isAlive = True
        self.image = pygame.image.load("assets/grenade.jpg")
        self.rect = self.image.get_rect()
        self.gravity =8,81
        self.timeToExplode = 5000
        self.time = 0
        self.collider = self.rect

    ##fonction qui calcul la trajectoire de la grenade et la fait se déplacer en fonction du temps
    def update(self, dt):
        self.time += dt
        distance = self.speed * (self.time / 1000)
        self.rect.x = self.owner.rect.x + distance * math.cos(math.radians(self.angle)) * self.direction
        self.rect.y = self.owner.rect.y - distance * math.sin(math.radians(self.angle)) + 0.5 * self.gravity * (self.time / 1000) ** 2 * self.direction
        if self.time >= self.timeToExplode:
            self.isAlive = False
            self.explode()

    def calculate_trajectory(self, time):
        # Convertir l'angle en radians
        angle_radians = math.radians(self.angle)
        
        # Calculer la vitesse initiale en x et en y
        velocity_x = self.speed * math.cos(angle_radians)
        velocity_y = self.speed * math.sin(angle_radians)
        
        # Calculer la position en x et en y du projectile à un instant donné
        pos_x = self.direction[0] + velocity_x * time
        pos_y = self.direction[1] + velocity_y * time - 0.5 * self.gravity * time**2
        
        # Prendre en compte le poids du projectile
        pos_y += 0.5 * self.weight * self.gravity * time**2
        
        return (pos_x, pos_y)
    
    def move(self, time_elapsed):
        # Calculer la nouvelle position du projectile
        new_pos = self.calculate_trajectory(time_elapsed)
        
        # Mettre à jour la position du projectile
        self.direction = new_pos
        self.collider.x = new_pos[0]
        self.collider.y = new_pos[1]
    
    def explode(self):
        #explosion
        pass
