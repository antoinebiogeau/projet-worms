import pygame
from game import Game
from player import Player
from weapon import weapon
import CONSTANT

pygame.init()

pygame.display.set_caption("worms")
screen = pygame.display.set_mode((640,480))

running = True
background = pygame.image.load("assets/bg.webp").convert()
game = Game()
game.player.rect.x = 100
game.player.rect.y = 100

while running:
    screen.blit(background, (0,0))
    screen.blit(game.player.image, game.player.rect)
    pygame.draw.rect(screen, CONSTANT.GROUND_COLOR, CONSTANT.GROUND_POSITION)
    ##appliquer la gravité au joueur c'est a dire le faire tomber si il n'est pas sur le sol 
    game.player.gravity()
    ##regarder si le joueur est en collision avec le sol
    ground = pygame.Rect(CONSTANT.GROUND_POSITION)
    game.player.collider(ground)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("droite")
                game.player.move_right()
            elif event.key == pygame.K_LEFT:
                print("gauche")
                game.player.move_left()
            elif event.key == pygame.K_UP:
                game.player.jump()
            elif event.key == pygame.K_SPACE:
                print("tirer")
                print(game.player.rect.x)
                print(game.player.rect.y)
                # Créer une instance de la classe weapon avec les paramètres appropriés
                p = weapon((0, 0), 100, None, 45, 100, 100)
                screen.blit(p.image, p.rect)
                p.move(10)
                
                # Ajouter le weapon à la liste des weapons du jeu
                game.weapons.append(p)
            elif event.key == pygame.K_x :
                print("change weapon")
                game.player.change_weapon()
            elif event.key == pygame.K_z :
                print("change perso")
                game.change_player()