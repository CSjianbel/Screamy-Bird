import os

import pygame

ASSETS_DIR = os.path.join('..', 'assets')
FONTS_DIR = os.path.join(ASSETS_DIR, 'fonts')

class Score:
    def __init__(self, bird_group, pipe_group):
        self.score = 0
        self.bird_group = bird_group
        self.pipe_group = pipe_group
        self.pass_pipe = False
        self.font = pygame.font.Font(os.path.join(FONTS_DIR, 'flappy-font.ttf'), 60)
        self.text = self.font.render(str(self.score), True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (100, 20)
        
    def update(self):
        if len(self.pipe_group) > 0:
            if self.bird_group.sprites()[0].rect.left > self.pipe_group.sprites()[0].rect.left \
                    and self.bird_group.sprites()[0].rect.right < self.pipe_group.sprites()[0].rect.right \
                    and not self.pass_pipe:
                self.pass_pipe = True

            if self.pass_pipe:
                if self.bird_group.sprites()[0].rect.left > self.pipe_group.sprites()[0].rect.right:
                    self.score += 1
                    self.pass_pipe = False

        self.text = self.font.render(str(self.score), True, (255, 255, 255))
    
    def draw(self, screen):
        screen.blit(self.text, (280, 40))

    def reset(self):
        self.score = 0