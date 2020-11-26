import pygame
pygame.font.init()

WIDTH = 620
HEIGHT = 480
SCREEN_SIZE = (WIDTH, HEIGHT)

TITLE = "RPG EXAMPLE PYGAME"
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCALE = 32

mapTileImage = {
    "G": pygame.transform.scale(pygame.image.load("images/Grass.png"), (SCALE, SCALE)),
    "S": pygame.transform.scale(pygame.image.load("images/Wood.png"), (SCALE, SCALE)),
    "R": pygame.transform.scale(pygame.image.load("images/Rock.png"), (SCALE, SCALE)),
}

dialogFont = pygame.font.SysFont('comicsans', 20)    #npcs dialogs

PLAYER_IMG = pygame.image.load("images/player/pl1.png")
NPC1_IMG = pygame.image.load("images/player/NPC1.png")
