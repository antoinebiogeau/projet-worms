class HealthBar(pygame.sprite.Sprite):
    def __init__(self, maxHealth):
        # Code d'initialisation existant ici
        self.image = pygame.Surface((100, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.maxWidth = self.rect.width
        
    def update(self, health):
        newWidth = (health / self.maxHealth) * self.maxWidth
        self.image = pygame.Surface((newWidth, 10))
        self.image.fill((255, 0, 0))