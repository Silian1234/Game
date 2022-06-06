import pygame, asyncio
import params, imports, menu
import NPS, dialogs
from config import cur, con


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(imports.player_image_right1, (params.WIDTH/24, params.HEIGHT/16))
        self.rect = self.image.get_rect()
        self.rect.x = params.WIDTH / 1.2
        self.rect.y = params.HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        self.animCountAD = 0
        self.animCountWS = 0
        self.walls = []
        self.activator = []
        self.NPSS = []
        self.dialog_window = []

    def update(self):
        if self.animCountAD + 1 >= 10:
            self.animCountAD = 0
        if self.animCountWS + 1 >= 12:
            self.animCountWS = 0
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_ESCAPE]:
            menu.start()
        if keystate[pygame.K_a]:
            self.speedx = -100
            self.image = imports.walkLeft[self.animCountAD // 5]
            self.animCountAD += 1
        if keystate[pygame.K_d]:
            self.speedx = 100
            self.image = imports.walkRight[self.animCountAD//5]
            self.animCountAD +=1
        if keystate[pygame.K_w]:
            self.speedy = -100
            self.image = imports.walkUp[self.animCountWS//4]
            self.animCountWS +=1
        if keystate[pygame.K_s]:
            self.speedy = 100
            self.image = imports.walkDown[self.animCountWS // 4]
            self.animCountWS += 1
        NowX = self.rect.x
        NowY = self.rect.y
        cur.execute(f"UPDATE PlayerPos SET xPos = {NowX}")
        cur.execute(f"UPDATE PlayerPos SET yPos = {NowY}")
        con.commit()
        for row in cur.execute(f"SELECT location, befLocation, newXPos, newYPos FROM PlayerPos"):
            if row[0] != row[1]:
                self.rect.y = row[3]
                self.rect.x = row[2]
            cur.execute(f"UPDATE PlayerPos SET befLocation = '{row[0]}'")
            con.commit()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > params.WIDTH:
            self.rect.right = params.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > params.HEIGHT:
            self.rect.bottom = params.HEIGHT
        if self.rect.bottom < params.HEIGHT/13:
            self.rect.bottom = params.HEIGHT/13

        for i in range(0, len(self.NPSS)):
            NPS = self.NPSS[i]
            bottomA = self.rect.bottom
            topA = self.rect.top
            rightA = self.rect.right
            leftA = self.rect.left

            bottomNPS = NPS.get_NPS_X() + NPS.get_NPS_Height()
            topNPS = NPS.get_NPS_X()
            leftNPS = NPS.get_NPS_Y()
            rightNPS = NPS.get_NPS_Y() + NPS.get_NPS_Width()

            if bottomA <= bottomNPS <= topA or bottomA <= topNPS <= topA:
                if leftNPS <= rightA and leftA <= rightNPS:
                    params.for_spawn_dialog_window = True

        for i in range(0, len(self.walls)):
            wall = self.walls[i]
            bottomA = self.rect.bottom
            topA = self.rect.top
            rightA = self.rect.right
            leftA = self.rect.left

            bottomB = wall.getY()+wall.getHeight()
            topB = wall.getY()
            leftB = wall.getX()
            rightB = wall.getX() + wall.getWidth()

            if bottomA <= topB:
                continue
            elif topA >= bottomB:
                continue
            elif rightA <= leftB:
                continue
            elif leftA >= rightB:
                continue
            self.rect.y = NowY
            self.rect.x = NowX
        """for i in range(0, len(self.activator)):
            activators = self.activator[i]
            bottomA = self.rect.bottom
            topA = self.rect.top
            rightA = self.rect.right
            leftA = self.rect.left

            bottomB = activators.getY() + activators.getHeight()
            topB = activators.getY()
            leftB = activators.getX()
            rightB = activators.getX() + activators.getWidth()

            if bottomA <= topB:
                continue
            elif topA >= bottomB:
                continue
            elif rightA <= leftB:
                continue
            elif leftA >= rightB:
                continue
            pygame.quit()"""

    def setWalls(self, walls):
        self.walls = walls

    def setActivator(self, activator):
        self.activator = activator

    def setNPSS(self, NPSS):
        self.NPSS = NPSS

    def setDialog(self, dialog_window):
        self.dialog_window = dialog_window

    def getY(self):
        return self.rect.y

    def getX(self):
        return self.rect.x

    def activatorChecker(self):
        for i in range(0, len(self.activator)):
            activators = self.activator[i]
            bottomA = self.rect.bottom
            topA = self.rect.top
            rightA = self.rect.right
            leftA = self.rect.left

            bottomB = activators.getY() + activators.getHeight()
            topB = activators.getY()
            leftB = activators.getX()
            rightB = activators.getX() + activators.getWidth()

            if bottomA <= topB:
                continue
            elif topA >= bottomB:
                continue
            elif rightA <= leftB:
                continue
            elif leftA >= rightB:
                continue
            return True