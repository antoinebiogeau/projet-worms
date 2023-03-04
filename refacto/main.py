import pygame
import Constant
from player import Player
from key import Key
from Projectile import Projectile
pygame.init()

pygame.display.set_caption("Worms")
screen = pygame.display.set_mode((640, 480))
pygame.time.Clock().tick(60)

isRunning = True
background = pygame.image.load("assets/bg.webp").convert()
terrain = pygame.image.load("assets/terrain.png").convert_alpha()
terrainMask = pygame.mask.from_surface(terrain)
playerOne = Player()
projectileInstances = []
projectileInstances.append(Projectile((200,0)))
projectileInstances.append(Projectile((300,0)))


while isRunning:
    screen.blit(background,(0,-100))
    screen.blit(terrain, (0,-200))
    screen.blit(terrainMask.to_surface(unsetcolor=(0,0,0,0),setcolor=(255,255,255,255)),(0,-200))
    #pygame.draw.rect(screen, Constant.GROUND_COLOR, Constant.GROUND_POSITION)
    
    playerOne.update(screen)
    for projectile in projectileInstances:
        projectile.update(screen)
        if projectile.collide(playerOne):
            projectileInstances.remove(projectile)
            del projectile
    
    #playerOne.drawColliders(screen)
    #playerOne.collide(terrainMask, (0,-200), screen)
    if playerOne.hp <=0:         
        isRunning = False
    ground = pygame.Rect(Constant.GROUND_POSITION)
    #playerOne.collide(ground)

    pygame.display.flip()
    #checkEvents
    Key().update()

pygame.quit()