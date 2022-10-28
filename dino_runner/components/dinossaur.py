import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD

DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}

JUMP_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}

RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}

#Local que o dino fica na tela baseado no y e x
X_POS = 80#Altura

Y_POS = 310#Largura

Y_POS_DUCK = 340#Aumenta a largura do dinossauro ao abaixar

JUMP_VEL = 8.5#Velocidade base do pulo


class Dinosaur(Sprite):

    def __init__(self):

        self.type = DEFAULT_TYPE

        self.image = RUN_IMG[self.type][0]

        self.dino_rect = self.image.get_rect()

        self.dino_rect.x = X_POS

        self.dino_rect.y = Y_POS

        self.step_index = 0

        self.dino_run = True

        self.dino_jump = False

        self.dino_duck = False

        self.jump_vel = JUMP_VEL

        self.setup_state()

    def setup_state(self):#Indica que o jogo começa sem power ups
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shiels_time_up = 0

    def update(self, user_input):#Baseado no input do jogador demonstra o output abaixo
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False

        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True

        elif not self.dino_jump and not self.dino_duck:#O jogo inica apenas correndo
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index  // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1 #Animação do dino, entre 0 e 5 roda a primeira foto e entre 5 e 10 a segunda

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.step_index += 1
        self.dino_duck = False

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))#Renderiza as imagens com os parametros de x e y 

