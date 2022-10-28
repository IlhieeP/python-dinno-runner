import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH #Hit box do obstaculo

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed#Diminui o valor do abstaculo - a velocidade do jogo

        if self.rect.x < -self.rect.width: 
            obstacles.pop()#Quando o obstaculo sair da tela a esquerda ele e removido

    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))#Renderiza os obstaculos
        

