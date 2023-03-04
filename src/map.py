import pygame

class Map:
    def __init__(self,screenHeight, screenWidth):
        self.terrainBase = "./assets/terrain.png"
        self.pixels = [[1] * screenHeight for i in range(screenWidth)]
        self.screenWidth = 600
        self.screenHeight = 300


    def generatePixel(self):
        self.terrain = pygame.transform.scale(pygame.image.load(self.terrainBase).convert(), (self.screenWidth, self.screenHeight))
        for i in range(self.screenWidth):
            for j in range(self.screenHeight):
                pixel = self.terrain.get_at((i,j))
                if (pixel == (0,0,0,255)):
                    self.pixels[i][j] = 0
                else:
                    self.pixels[i][j] = 1

    def regenPixels(self,x,y,area):
        xStart = 0 if x - area < 0 else x - area
        xEnd = self.screenWidth if x + area > self.screenHeight else x + area
        yStart = 0 if y - area < 0 else y - area
        yEnd = self.screenH if y + area > self.screenH else y + area

        for i in range(xStart, xEnd):
            for j in range(yStart, yEnd):
                pixel = self.terrain.get_at((i,j))
                if pixel == (0,0,0,255):
                    self.pixels[i][j] = 0
                else:
                    self.pixels[i][j] = 1
    
    def destroy(self, xOrigin,yOrigin, area):
        x = xOrigin
        y = yOrigin
        pygame.draw.circle(self.terrain, (0,0,0,255), (x,y), area)
        self.regenPixels(x,y,area) 