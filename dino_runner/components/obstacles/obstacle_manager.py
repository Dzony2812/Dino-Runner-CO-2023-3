from dino_runner.components.obstacles.cactus import Cactus

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus())
        for obstace in self.obstacles:
            if obstace.rect.x <- obstace.rect.width:
                self.obstacles.remove(obstace)
            obstace.update(game_speed, player)

    def draw(self, screen):
        for obstace in self.obstacles:
            obstace.draw(screen)