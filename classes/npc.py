import config
import pygame

class Npc:
    def __init__(self, x, y, textMessage, wantsToFight):
        self.position = [x, y]
        self.img = pygame.transform.scale(config.NPC1_IMG, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)
        self.textMessage = textMessage
        self.wantsToFight = wantsToFight

    def render(self, screen, camera):
        self.rect = pygame.Rect(self.position[0] * config.SCALE - (camera[0] * config.SCALE), self.position[1] * config.SCALE - (camera[1] * config.SCALE), config.SCALE,config.SCALE)  # STORING RECTANGLE COORS OF PLAYER
        screen.blit(self.img, self.rect)

    def Battle(self, player):
        pass
    def interact(self, screen, Player):
        Text = config.dialogFont.render(self.textMessage, 1, (config.BLACK))
        screen.blit(Text, (config.WIDTH/2 - Text.get_width(), config.HEIGHT - 100))

        if self.wantsToFight == 1:
            self.Battle()
        else:
            return

