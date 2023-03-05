import pygame
import Constant
from key import Key
from Projectile import Projectile
from Text import Text

class Player(pygame.sprite.Sprite):
    def __init__(self, position, team):
        super().__init__()
        self.hp = 100
        self.isCurrent = False
        self.actions = {
            "walk_left": False,
            "walk_right": False,
            "jump": False,
            "shooting_stance": False
        }
        self.velocity = {
            "x": 0,
            "y": 0
        }
        self.constraints = {
            "isFalling": True
        }
        self.projectiles = []
        
        self.image = pygame.image.load("assets/character.png")
        self.rect = self.image.get_rect()
        self.time = 0
        self.collider = {
            "mask": pygame.Mask((self.rect.width - 10, self.rect.height * 0.15)),
            "offset": (self.rect.x + 5, self.rect.y + self.rect.height * 0.9 + 2),
        }
        self.xAngle = 50
        self.yAngle = -50
        self.force = 1
        self.isShooting = False
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.team = team
        self.canShoot = True
        self.currentWeapon = 0
        self.imageFacing = "right"

    def update(self, screen):
        if self.isCurrent:
            self.checkActions()
            self.jump()
            #draw UI
        if self.constraints["isFalling"]:
            self.rect.y += 3 + self.velocity["y"]
        else:
            self.rect.y += self.velocity["y"]
        if not self.actions["shooting_stance"] and self.isCurrent:
            self.rect.x += 2 if self.actions["walk_right"] else -2 if  self.actions["walk_left"] else 0
            #print(self.constraints["isFalling"])
        if self.actions["shooting_stance"]:
            pygame.draw.line(screen, (255,0,0), (self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2),  (self.rect.x + self.rect.width/2 + self.xAngle, self.rect.y + self.rect.height/2 + self.yAngle))
        if self.actions["walk_left"] and self.imageFacing == "right":
            self.image = pygame.transform.flip(self.image, True, False)
            self.imageFacing = "left"
        if self.actions["walk_right"] and self.imageFacing == "left":
            self.image = pygame.transform.flip(self.image, True, False)
            self.imageFacing = "right"
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255,0,0) if self.team == 0 else (0,0,255), (self.rect.x, self.rect.y - 10, self.rect.width  * (self.hp / 100), 5))
        pygame.draw.rect(screen, (100,0,0) if self.team == 0 else (0,0,100), (self.rect.x, self.rect.y - 10, self.rect.width, 5), 1)
        Text().render(screen, "Hp : " + str(self.hp), (self.rect.x, self.rect.y - 30), (100,0,0) if self.team == 0 else (0,0,100))
        weaponText = f"Weapon : { 'grenade' if self.currentWeapon == 1 else 'rocket'}"
        Text().render(screen, weaponText, (20,10),(20,20,20), bigFont=True)
    def collide(self):
        if self.rect.y + self.rect.height > Constant.GROUND_LEVEL:
            self.constraints["isFalling"] = False
        else:
            self.constraints["isFalling"] = True

    
    def checkActions(self):
            if Key().get_key_down(pygame.K_RIGHT) and not self.actions["walk_left"]:
                self.actions["walk_right"] = True
            else:
                self.actions["walk_right"] = False
            if Key().get_key_down(pygame.K_LEFT) and not self.actions["walk_right"]:
                self.actions["walk_left"] = True
            else:
                self.actions["walk_left"] = False
            if Key().get_key_down(pygame.K_UP) and not self.actions["jump"] and not self.constraints["isFalling"]:
                self.actions["jump"] = True
            if Key().get_key_down(pygame.K_SPACE):
                self.hp -= 0.1
            if Key().get_key_down(pygame.K_f):
                self.actions["shooting_stance"] = True
            else:
                self.actions["shooting_stance"] = False
            if self.actions["shooting_stance"]:
                if (Key().get_key_down(pygame.K_LEFT)):
                    if (self.xAngle > - 100):
                        self.xAngle -= 1
                        self.yAngle -= 1 if self.xAngle > 0 else -1   
                if (Key().get_key_down(pygame.K_RIGHT)):
                    if (self.xAngle < 100):
                        self.xAngle += 1
                        self.yAngle -= 1 if self.xAngle < 0 else -1



        #if shift pressed, put player in shoot stance
        #right and left changes the angle
        #else if stance is shooting, then shoot projectile at choosen angle
        #else do nothing


    def jump(self):
        if self.actions["jump"]:
            self.velocity["y"] = -5
            self.time += 0.1
        if self.time > 2:
            self.velocity["y"] = 0
            self.actions["jump"] = False
        if self.constraints["isFalling"] == False:
            self.time = 0

    def shoot(self):
        if self.actions["shooting_stance"] and self.canShoot:
            if Key().get_key_down(pygame.K_r):
                print("shooting")
                self.actions["shooting_stance"] = False
                self.canShoot = False
                return Projectile((self.rect.x + self.rect.width / 2 + self.xAngle, self.rect.y + self.rect.height / 2 + self.yAngle), (self.xAngle / 10, self.yAngle / 10))


    def drawColliders(self, screen):
        screen.blit(self.collider["mask"].to_surface(setcolor=(0,255,0,255)), (self.rect.x + 5, self.rect.y + self.rect.height))