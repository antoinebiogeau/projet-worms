import pygame
from pygame.locals import *
import random
from map import Map
from player import Player

# Initialisation de pygame
pygame.init()

# Définition des constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRAVITY = 0.2
FPS = 60

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Worms")

# Création des sprites
allSprites = pygame.sprite.Group()
players = pygame.sprite.Group()
weapons = pygame.sprite.Group()

player1 = Player("player1", RED, 100, 100)
player2 = Player("player2", BLUE, 500, 100)

allSprites.add(player1)
allSprites.add(player2)
players.add(player1)
players.add(player2)
##cree la map
Map = Map(200,200)

# Boucle de jeu
clock = pygame.time.Clock()
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE:
                player1.jump()

    # Mise à jour des sprites
    dt = clock.tick(FPS)
    allSprites.update(dt,  Map.pixels) ##erreur la 
    projectiles.update(dt)

    # Gestion des collisions entre les joueurs et les projectiles
    hits = pygame.sprite.groupcollide(players, projectiles, False, True)
    for player, projectiles in hits.items():
        for projectile in projectiles:
            player.takeDamage(projectile.damage)

    # Affichage
    screen.fill(WHITE)
    allSprites.draw(screen)
    projectiles.draw(screen)
    pygame.display.flip()

# Fermeture de pygame
pygame.quit()
