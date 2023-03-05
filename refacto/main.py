import pygame
import Constant
from player import Player
from key import Key
from Projectile import Projectile
from wind import Wind
from Text import Text

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

groundCollider = pygame.Rect(Constant.GROUND_POSITION)

#pygame.time.set_timer(pygame.USEREVENT+1,5)
PLAYER_SWITCH_EVENT = pygame.USEREVENT + 1
WIND_SWITCH_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(WIND_SWITCH_EVENT, 5000)


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
    if playerOne.isCurrent:
        weaponText = f"Weapon : { 'grenade' if playerOne.currentWeapon == 1 else 'rocket'}"
        Text().render(screen, weaponText, (20,10),(20,20,20), bigFont=True)
    else:
        weaponText = f"Weapon : { 'grenade' if playerTwo.currentWeapon == 1 else 'rocket'}"
        Text().render(screen, weaponText, (20,10),(20,20,20), bigFont=True)
    potentialShoot = playerOne.shoot() if playerOne.isCurrent else playerTwo.shoot()
    if potentialShoot is not None:
        projectileInstances.append(potentialShoot)
        pygame.time.set_timer(PLAYER_SWITCH_EVENT, 1000, True)
        potentialShoot = None
    for projectile in projectileInstances:
        projectile.update(screen)
        if projectile.collide(playerOne) or projectile.collide(playerTwo) or projectile.collide(groundCollider, 0) or projectile.rect.x < -1000 or projectile.rect.x > 1000 or projectile.rect.y > 500:
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
    if playerOne.hp <= 0 or playerTwo.hp <= 0:
        isRunning = False
    pygame.display.flip()
    #checkEvents
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == PLAYER_SWITCH_EVENT:
            switchPlayer()
        if event.type == WIND_SWITCH_EVENT:
            Wind().update()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            if playerOne.isCurrent:
                playerOne.currentWeapon = 1 if playerOne.currentWeapon == 0 else 0
            else:
                playerTwo.currentWeapon = 1 if playerTwo.currentWeapon == 0 else 0
    
    Key().update()
    clock.tick(60)
pygame.quit()


            