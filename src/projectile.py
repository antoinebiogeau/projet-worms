import math
import pygame


class projectile():
    def __init__(self, direction, speed, damage, owner , type, puissance, angle):
        self.direction = direction
        self.speed = speed
        self.damage = damage
        self.puissance = puissance
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
            
        elif type == "GSF":
            self.image = pygame.image.load("assets/graphics/grenade.png")
            self.rect = self.image.get_rect()
            self.gravity = 0.2
            self.timeToExplode = 5000
            self.startTime = pygame.time.get_ticks()
            
        elif type == "RK":
            self.image = pygame.image.load("assets/graphics/rocket.png")
            self.rect = self.image.get_rect()
            self.gravity = 0.2
            self.wind = 0.0  # Vent à appliquer
            self.explosionRadius = 64  # Rayon de l'explosion
            self.hasExploded = False

    def update(self, dt):
        if self.type == "GF" or self.type == "GSF":
            # Calcul de la position de la grenade en fonction du temps et de la gravité
            timeSinceStart = pygame.time.get_ticks() - self.startTime
            distance = self.speed * (timeSinceStart / 1000)
            self.rect.x = self.owner.rect.x + distance * math.cos(math.radians(self.angle)) * self.direction
            self.rect.y = self.owner.rect.y - distance * math.sin(math.radians(self.angle)) + 0.5 * self.gravity * (timeSinceStart / 1000) ** 2 * self.direction
            
            # Vérification si la grenade doit exploser
            if timeSinceStart >= self.timeToExplode:
                self.isAlive = False
                self.explode()
        elif self.type == "RK":
            # Calcul de la position de la roquette en fonction du temps, du vent et de la gravité
            self.speed += self.wind * dt / 1000
            distance = self.speed * (dt / 1000)
            self.rect.x += distance * math.cos(math.radians(self.angle)) * self.direction
            self.rect.y -= distance * math.sin(math.radians(self.angle)) + 0.5 * self.gravity * (dt / 1000) ** 2 * self.direction
            
            # Vérification si la roquette a touché quelque chose
            collidingSprites = pygame.sprite.spritecollide(self, allSprites, False)
            for sprite in collidingSprites:
                if sprite != self.owner:
                    self.isAlive = False
                    self.hasExploded = True
                    self.explode()
                    
            # Vérification si la roquette doit exploser
            if self.hasExploded:
                collidingSprites = pygame.sprite.spritecollide(self, allSprites, False)
                for sprite in collidingSprites:
                    if sprite != self.owner and math.sqrt((self.rect.centerx - sprite.rect.centerx) ** 2 + (self.rect.centery - sprite.rect.centery) ** 2) <= self.explosionRadius:
                        sprite.isAlive = False
                        self.explode()

    def explode(self):
        # Trouver tous les sprites dans le rayon de l'explosion
        spritesInRadius = []
        for sprite in allSprites:
            distance = math.sqrt((self.rect.centerx - sprite.rect.centerx) ** 2 + (self.rect.centery - sprite.rect.centery) ** 2)
            if distance <= self.explosionRadius and sprite != self.owner:
                spritesInRadius.append(sprite)
        
        # Appliquer les dégâts à tous les sprites dans le rayon de l'explosion
        for sprite in spritesInRadius:
            sprite.takeDamage(self.damage)
        
        # Supprimer le projectile
        self.kill()



