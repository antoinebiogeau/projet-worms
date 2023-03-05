import pygame
import Constant
from player import Player
from key import Key
from Projectile import Projectile
from wind import Wind

pygame.init()

pygame.display.set_caption("Worms")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

isRunning = True
background = pygame.image.load("assets/bg.webp").convert()
terrain = pygame.image.load("assets/terrain.png").convert_alpha()
terrainMask = pygame.mask.from_surface(terrain)
playerOne = Player((20,0), 0)
playerTwo = Player((220,0), 1)
Players = [playerOne, playerTwo]
current_player = 0
playerOne.isCurrent = True 

projectileInstances = []

#pygame.time.set_timer(pygame.USEREVENT+1,5)
PLAYER_SWITCH_EVENT = pygame.USEREVENT + 1


def switchPlayer():
    print("Switching players")
    if playerOne.isCurrent:
        playerOne.isCurrent = not playerOne.isCurrent   
        playerTwo.isCurrent = True
        playerTwo.canShoot = True        
    else:
        playerTwo.isCurrent = not playerTwo.isCurrent
        playerOne.isCurrent = True
        playerOne.canShoot = True  

while isRunning:
    screen.blit(background,(0,-100))
    screen.blit(terrain, (0,0))
    #screen.blit(terrainMask.to_surface(unsetcolor=(0,0,0,0),setcolor=(255,255,255,255)),(0,-200))
    pygame.draw.rect(screen, Constant.GROUND_COLOR, Constant.GROUND_POSITION)
    
    playerOne.update(screen)
    playerTwo.update(screen)
    potentialShoot = playerOne.shoot() if playerOne.isCurrent else playerTwo.shoot()
    if potentialShoot is not None:
        projectileInstances.append(potentialShoot)
        pygame.time.set_timer(PLAYER_SWITCH_EVENT, 1000, True)
        potentialShoot = None
    for projectile in projectileInstances:
        projectile.update(screen)
        if projectile.collide(playerOne) or projectile.collide(playerTwo) or projectile.rect.x < -1000 or projectile.rect.x > 1000 or projectile.rect.y > 500:
            projectileInstances.remove(projectile)
            del projectile
    

    #playerOne.drawColliders(screen)
    playerOne.collide()
    playerTwo.collide()
    ground = pygame.Rect(Constant.GROUND_POSITION)
    #playerOne.collide(ground)
    if Players[current_player].hp <= 0:
        current_player.isCurrent = False
        current_player = (current_player + 1) % len(Players)
        current_player.isCurrent = True
    if all(player.hp <= 0 for player in Players):
        isRunning = False
    pygame.display.flip()
    #checkEvents
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == PLAYER_SWITCH_EVENT:
            switchPlayer()
    Key().update()
    
    clock.tick(60)
pygame.quit()


            