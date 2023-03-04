import math
import pygame


class projectile():
    def __init__(self, direction, speed, damage, owner , type, angle):
        self.direction = direction
        self.speed = speed
        self.damage = damage
        self.weight = 0
        self.angle = angle
        self.owner = owner
        self.collider = Rect(self.x, self.y, 32,32)
        self.isAlive = True
        if type == "GF":
            self.image = pygame.image.load("assets/graphics/grenade.png")
            self.rect = self.image.get_rect()
            self.gravity =8,81  # Gravité à appliquer
            self.timeToExplode = 5000  # Temps en millisecondes avant explosion
            self.startTime = pygame.time.get_ticks()  # Temps de création de la grenade
            weight = 10
            
        elif type == "GSF":
            self.image = pygame.image.load("assets/graphics/grenade.png")
            self.rect = self.image.get_rect()
            self.gravity = 0.2
            self.timeToExplode = 5000
            self.startTime = pygame.time.get_ticks()
            weight = 10
            
        elif type == "RK":
            self.image = pygame.image.load("assets/graphics/rocket.png")
            self.rect = self.image.get_rect()
            self.gravity = 0.2
            self.wind = 0.0  # Vent à appliquer
            self.explosionRadius = 64  # Rayon de l'explosion
            self.hasExploded = False
            self.weight = 10

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