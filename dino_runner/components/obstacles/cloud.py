import random
from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD

class Cloud:
    X_POS = 30
    Y_POS = 1200
    def __init__(self):
        self.image = CLOUD
        self.width = self.image.get_width ()
        self.x = SCREEN_WIDTH + random.randint (800, 1000)
        self.y = random.randint(50, 100)
        self.cloud_speed = 14
        
        
    def update(self):
        self.x -= self.cloud_speed
        if self.x < - self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
      screen.blit(self.image, (self.x, self.y))