import pygame
import constant
from player import Player
from key import Key
from projectile import Projectile
from wind import Wind
from Text import Text
from Menu import Menu
from GameOver import Restart

pygame.init()

pygame.display.set_caption("Worms")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

isRunning = True
background = pygame.image.load("assets/bg.webp").convert()
terrain = pygame.image.load("assets/terrain.png").convert_alpha()
terrainMask = pygame.mask.from_surface(terrain)
playerOne = Player((20,0), 0)
playerOneSecond = Player((30,0),0)
playerTwo = Player((220,0), 1)
playerTwoSecond = Player((210,0), 1)
PlayerThree = Player((420,0), 2)
PlayerThreeSecond = Player((410,0), 2)
Players = [playerOne, playerTwo, PlayerThree, playerOneSecond, playerTwoSecond, PlayerThreeSecond]
current_player = 0
playerOne.isCurrent = True 
menu = True
playing = False
running = True
Gameover = False

projectileInstances = []

groundCollider = pygame.Rect(constant.GROUND_POSITION)

#pygame.time.set_timer(pygame.USEREVENT+1,5)
PLAYER_SWITCH_EVENT = pygame.USEREVENT + 1
WIND_SWITCH_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(WIND_SWITCH_EVENT, 5000)


def switchPlayer():
    global current_player
    print(current_player)
    Players[current_player].isCurrent = not Players[current_player].isCurrent
    current_player += 1
    if current_player >= len(Players):
        current_player = 0
    while(Players[current_player].hp <= 0):
        if Players[current_player].hp <= 0:
            current_player += 1
        if current_player >= len(Players):
            current_player = 0
    Players[current_player].isCurrent = True
    Players[current_player].canShoot = True
    
    print("Switching players")

def inTurnSwitch():
    global current_player
    global Players
    currentTeam = Players[current_player].team
    for i in range(len(Players)):
        if Players[i].team == currentTeam and i != current_player:
            Players[current_player].isCurrent = False
            Players[current_player].canShoot = False
            Players[current_player], Players[i] = Players[i], Players[current_player]
            Players[current_player].isCurrent = True
            Players[current_player].canShoot = True

def checkVictory():
    global Players
    deaths = [0,0,0]
    for player in Players:
        if player.hp <= 0:
            deaths[player.team] += 1
    if deaths[0] == 2 and deaths[1] == 2 and deaths[2] < 2:
        return "G"
    elif deaths[0] == 2 and deaths[1] < 2 and deaths[2] == 2:
        return "B"
    elif deaths[0] < 2 and deaths[1] == 2 and deaths[2] == 2:
        return "R"
    elif deaths[0] == 2 and deaths[1] == 2 and deaths[2] == 2:
        return "N"
    else:
        return None
 
while isRunning:
    while menu:
        play_button_pos = (screen.get_width() / 2 - 50, screen.get_height() / 2)
        quit_button_pos = (screen.get_width() / 2 - 50, screen.get_height() / 2 + 50)
        try:
            Menu()
        except Exception as exception:
            print("Une erreur inattendue s'est produite :", exception)


        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_pos[0] < pygame.mouse.get_pos()[0] < play_button_pos[0] + 100 and play_button_pos[1] < \
                        pygame.mouse.get_pos()[1] < play_button_pos[1] + 50:
                    menu = False
                    playing = True
                elif quit_button_pos[0] < pygame.mouse.get_pos()[0] < \
                        quit_button_pos[0] + 100 and quit_button_pos[1] < pygame.mouse.get_pos()[1] < quit_button_pos[
                    1] + 50:
                    running = False
                    menu = False
    while running:
        screen.blit(background,(0,-100))
        screen.blit(terrain, (0,0))
        #screen.blit(terrainMask.to_surface(unsetcolor=(0,0,0,0),setcolor=(255,255,255,255)),(0,-200))
        pygame.draw.rect(screen, constant.GROUND_COLOR, constant.GROUND_POSITION)
        for player in Players:
            player.update(screen)
            player.collide()
        ground = pygame.Rect(constant.GROUND_POSITION)
        weaponText = f"Weapon : {'grenade' if Players[current_player].currentWeapon == 1 else 'light-grenade' if Players[current_player].currentWeapon == 2 else 'rocket'}"
        Text().render(screen, weaponText, (20,10),(20,20,20), bigFont=True)
        potentialShoot = Players[current_player].shoot()
        if potentialShoot is not None:
            projectileInstances.append(potentialShoot)
            pygame.time.set_timer(PLAYER_SWITCH_EVENT, 1000, True)
            potentialShoot = None
        for projectile in projectileInstances:
            projectile.update(screen)
            projectile.collide(playerOne)
            projectile.collide(playerTwo)
            projectile.collide(PlayerThree)
            projectile.collide(ground, 0)
            if projectile.explode(screen, Players) or projectile.rect.x < -1000 or projectile.rect.x > 1000 or projectile.rect.y > 500:
                pygame.display.flip()

                projectileInstances.remove(projectile)
                del projectile
        

        #playerOne.drawColliders(screen)
        
        #playerOne.collide(ground)

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
                    playerOne.currentWeapon += 1
                    if playerOne.currentWeapon > 2:
                        playerOne.currentWeapon = 0
                else:
                    playerTwo.currentWeapon += 1
                    if playerTwo.currentWeapon > 2:
                        playerTwo.currentWeapon = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                inTurnSwitch()           
    
        Key().update()
        print(checkVictory())
        if checkVictory() is not None:
            Gameover = True
            break
        clock.tick(60)
    while Gameover:
        quit_button_pos = (screen.get_width() / 2 - 50, screen.get_height() / 2 + 50)
        try:
            Restart(checkVictory())
        except Exception as exception:
            print("Une erreur inattendue s'est produite :", exception)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Gameover = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button_pos[0] < pygame.mouse.get_pos()[0] < \
                        quit_button_pos[0] + 100 and quit_button_pos[1] < pygame.mouse.get_pos()[1] < quit_button_pos[
                    1] + 50:
                    running = False
                    Gameover = False
                    isRunning = False
pygame.quit()


            