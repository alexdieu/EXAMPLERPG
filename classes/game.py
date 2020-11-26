import pygame
import math
import config

from classes.player import Player
from classes.npc import Npc
from enum import Enum


class GameStat(Enum):
    NONE = 0
    RUNNING = 1
    ENDED = 2

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.gameState = GameStat.NONE
        self.objects = []
        self.map = []
        self.cameraX = 0
        self.camera = [0, 0]
    def setUp(self):
        player = Player(1, 1)
        npc1 = Npc(3, 7, "BLAAAAAA I AM NPC1 ! i am gonna eat u", 0)
        self.player = player
        self.npc1 = npc1
        self.objects.append(player)
        self.objects.append(npc1)
        self.gameState = GameStat.RUNNING
        self.conversation = None

        self.loadMap("map1")


    def update(self):
        self.screen.fill(config.BLACK)
        self.renderMap(self.screen)
        self.keyEvents()
        self.player.render(self.screen, self.camera)
        for obj in self.objects[1:]:
            obj.render(self.screen, self.camera)
            if self.conversation == True:
                obj.interact(self.screen, self.player)

        pygame.display.update()


    def keyEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameState = GameStat.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameState = GameStat.ENDED

                elif (event.key == pygame.K_w or event.key == pygame.K_UP):
                    self.moveUnit(self.player, [0, -1])
                elif (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                    self.moveUnit(self.player, [0, 1])
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                    self.moveUnit(self.player, [-1, 0])
                elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                    self.moveUnit(self.player, [1, 0])

    def loadMap(self, map):
        with open("maps/" + map + ".txt") as mapFile:
            for line in mapFile:
                tiles = []
                self.cameraX = 0
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                    self.cameraX += 1

                self.map.append(tiles)

    def CameraPos(self):

        maxXPos = self.cameraX - config.WIDTH / config.SCALE
        xPos = self.player.position[0] - math.ceil(round(config.WIDTH / config.SCALE / 2))

        if xPos <= maxXPos and xPos >= 0:
            self.camera[0] = xPos
        elif xPos < 0:
            self.camera[0] = 0
        else:
            self.camera[0] = maxXPos

        # Y Position
        maxYPos = len(self.map) - config.HEIGHT / config.SCALE
        yPos = self.player.position[1] - math.ceil(round(config.WIDTH / config.SCALE / 2))

        if yPos <= maxYPos and yPos >= 0:
            self.camera[1] = yPos
        elif yPos < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = maxYPos

    def renderMap(self, screen):
        self.CameraPos()
        y_pos = 0

        for line in self.map:
            x_pos = 0
            for tile in line:
                image = config.mapTileImage[tile]
                rect = pygame.Rect(x_pos * config.SCALE - (self.camera[0] * config.SCALE),
                                   y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos += 1
            y_pos += 1

    def moveUnit(self, unit, ChangePos):
        newPosition = [unit.position[0] + ChangePos[0], unit.position[1] + ChangePos[1]]

        self.conversation = False

        for obj in self.objects:
            if newPosition[0] == obj.position[0] and newPosition[1] == obj.position[1]:
                self.conversation = True
                return

        if newPosition[0] < 0 or newPosition[0] > (len(self.map[0]) - 1):
            return
        if newPosition[1] < 0 or newPosition[1] > (len(self.map[0]) - 1):
            return
        if self.map[newPosition[1]][newPosition[0]] == "S":
            return
        unit.updatePosition(newPosition)
    def displayNpcMessage(self, unit):
        unit.interact(self.screen, self.player)

