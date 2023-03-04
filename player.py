import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, name, color):
        super().__init__()
        self.name = name
        self.color = color
        self.velocity = 5
        self.health = 100
        self.gravity_f = 0.6
        self.image = pygame.image.load("assets/character.png")    
        self.rect  = self.image.get_rect()
        self.current_weapon = "GSF"
        self.time = 0
        self.is_jumping = False

    def move_right(self):
        self.rect.x += self.velocity
    
    def move_left(self):
        self.rect.x -= self.velocity

    def jump(self):
        self.is_jumping = True
        if self.is_jumping:
            self.rect.y -= 1
            self.time += 0.5
        if self.time > 3:
            self.is_jumping = False
        
    
    def gravity(self):
        self.rect.y += self.gravity_f 
    def collider(self, ground):
        if self.rect.y == ground.y:
            # Le joueur est en contact avec le sol
            self.gravity_f  = 0