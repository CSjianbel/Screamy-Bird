import os

import pygame

ASSETS_DIR = os.path.join('..', 'assets')
SPRITES_DIR = os.path.join(ASSETS_DIR, 'sprites')

class Sprites:
    def __init__(self):
        self.bird = tuple([
            pygame.image.load(os.path.join(SPRITES_DIR, f'cat{i}.png'))
            for i in range(1, 7)
        ])
        self.background = pygame.image.load(os.path.join(SPRITES_DIR, 'background.png'))
        self.pipe = pygame.image.load(os.path.join(SPRITES_DIR, 'pipe.png'))
        self.ground = pygame.image.load(os.path.join(SPRITES_DIR, 'ground.png'))