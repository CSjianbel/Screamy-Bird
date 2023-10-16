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
        self.save_button = pygame.image.load(os.path.join(SPRITES_DIR, 'restart.png'))
        self.leaderboard = pygame.image.load(os.path.join(SPRITES_DIR, 'leaderboard.png'))
        self.leaderboard_table = pygame.image.load(os.path.join(SPRITES_DIR, 'leaderboard_table.png'))
        self.result = pygame.image.load(os.path.join(SPRITES_DIR, 'result.png'))
        self.game_over = pygame.image.load(os.path.join(SPRITES_DIR, 'game_over.png'))
        self.get_ready = pygame.image.load(os.path.join(SPRITES_DIR, 'get_ready.png'))
        self.restart_btn = pygame.image.load(os.path.join(SPRITES_DIR, 'restart.png'))
        self.home_btn = pygame.image.load(os.path.join(SPRITES_DIR, 'home.png'))
        self.show_board_btn = pygame.image.load(os.path.join(SPRITES_DIR, 'show_board.png'))
        self.back_btn = pygame.image.load(os.path.join(SPRITES_DIR, 'back.png'))
        self.submit_btn = pygame.image.load(os.path.join(SPRITES_DIR, 'submit.png'))
        self.name_input = pygame.image.load(os.path.join(SPRITES_DIR, 'name_input.png'))
        self.name_input_placeholder = pygame.image.load(os.path.join(SPRITES_DIR, 'name_input_placeholder.png'))