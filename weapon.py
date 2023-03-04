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
        self.gravity =8.81
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

    def calculate_trajectory(self, x0, y0, v0, angle_degrees, gravity):
        # Convertir l'angle en radians
        angle_radians = math.radians(angle_degrees)

        # Calculer la vitesse initiale en x et en y
        velocity_x = v0 * math.cos(angle_radians)
        velocity_y = v0 * math.sin(angle_radians)

        # Calculer le temps de vol
        time_of_flight = 2 * v0 * math.sin(angle_radians) / gravity

        # Créer un tableau pour stocker les positions du projectile
        positions = []

        # Boucle pour calculer les positions du projectile à différents instants
        for t in range(0, int(time_of_flight * 1000), 10):
            # Convertir le temps en secondes
            t_sec = t / 1000.0

            # Calculer la position en x et en y du projectile à un instant donné
            pos_x = x0 + velocity_x * t_sec
            pos_y = y0 + velocity_y * t_sec - 0.5 * gravity * t_sec**2

            # Ajouter la position à la liste
            positions.append((pos_x, pos_y))

        return positions

    def move(self, dt):
        # Calculer la position actuelle du projectile
        self.time = 0
        for i in range(0, dt):
            self.time += 1
            print(self.time)
            pos_x = self.x + self .speed * math.cos(math.radians(self.angle)) * (self.time)
            pos_y = self.y - self.speed * math.sin(math.radians(self.angle)) * (self.time) + 0.5 * self.gravity * (self.time / 1000) ** 2 
            print(pos_x, pos_y)

            # Mettre à jour la position et la collider du projectile
            self.rect.x = pos_x
            self.rect.y = pos_y
            self.collider = self.rect

            # Si le projectile a atteint le temps d'explosion, le faire exploser
            if self.time >= self.timeToExplode:
                self.isAlive = False
                self.explode()
    
    
    def explode(self):
        #explosion
        pass
