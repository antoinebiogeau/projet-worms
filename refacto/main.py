import pygame
import Constant
from player import Player
from key import Key
pygame.init()

pygame.display.set_caption("Worms")
screen = pygame.display.set_mode((640, 480))
pygame.time.Clock().tick(60)

isRunning = True
background = pygame.image.load("assets/bg.webp").convert()

playerOne = Player()


while isRunning:
    screen.blit(background,(0,0))
    pygame.draw.rect(screen, Constant.GROUND_COLOR, Constant.GROUND_POSITION)
   
    playerOne.update(screen)
    if playerOne.hp <=0:         
        isRunning = False
    ground = pygame.Rect(Constant.GROUND_POSITION)
    playerOne.collide(ground)

    pygame.display.flip()
    #checkEvents
    Key().update()

pygame.quit()