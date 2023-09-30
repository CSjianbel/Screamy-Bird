import pygame

class Sprites:
    def __init__(self):
        self.bird = (
            pygame.image.load("../assets/sprites/bird1.png"),
            pygame.image.load("../assets/sprites/bird2.png"),
            pygame.image.load("../assets/sprites/bird3.png"),
        )
        self.background = pygame.image.load("../assets/sprites/background.png")
        self.pipe = pygame.image.load("../assets/sprites/pipe.png")
        self.ground = pygame.image.load("../assets/sprites/ground.png")
        self.save_button = pygame.image.load("../assets/sprites/restart.png")