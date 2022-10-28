import random
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud:
    def __init__(self):
        self.cloud = CLOUD
        self.x = SCREEN_WIDTH + random.randint(2500, 3000)
        self.y = random.randint(50, 100)
        self.image = self.cloud
        self.width = self.image.get_width()
 
    def update(self, game_speed):
        self.x -= game_speed #O background se move mais rapido que as nuvens
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)
            
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))