import pygame
import random

from game.entities.ground import Ground
from game.entities.background import Background
from game.entities.bird import Bird
from game.entities.pipe import Pipe
from game.entities.score import Score

class GameState:
    def __init__(self, config, game_status):
        self.config = config
        self.screen = self.config.screen
        self.sprites = self.config.sprites
        self.pipe_frequency = 1500
        self.last_pipe = pygame.time.get_ticks() - self.pipe_frequency
        self.game_status = game_status
        self.bird_group = pygame.sprite.Group()
        self.pipe_group = pygame.sprite.Group()
        self.ground_group = pygame.sprite.Group()
        self.bird = Bird(self.sprites.bird, 100, int(self.config.window.height / 2), self.game_status)
        self.ground = Ground(self.sprites.ground, 300, 768, self.game_status)
        self.background = Background(self.sprites.background)
        self.score = Score(self.bird_group, self.pipe_group)
        self.pass_pipe = False
        self.ground_group.add(self.ground)
        self.bird_group.add(self.bird)

    def update(self):
        self.background.draw(self.screen)
        self.pipe_group.draw(self.screen)
   
        self.bird_group.draw(self.screen)
        self.bird_group.update()
        
        self.score.draw(self.screen)
        self.score.update()

        if self.game_status.is_game_started:
            self.generate_pipes()
            self.check_collisions()

        self.ground_group.draw(self.screen)
        self.ground_group.update()

    def generate_pipes(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_pipe > self.pipe_frequency:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(self.sprites.pipe, self.config.window.width, int(self.config.window.height / 2) + pipe_height, -1)
            top_pipe = Pipe(self.sprites.pipe, self.config.window.width, int(self.config.window.height / 2) + pipe_height, 1)
            self.pipe_group.add(btm_pipe)
            self.pipe_group.add(top_pipe)
            self.last_pipe = time_now
        self.pipe_group.update()

    def check_collisions(self):
        if  pygame.sprite.groupcollide(self.bird_group, self.pipe_group, False, False) or \
            pygame.sprite.groupcollide(self.bird_group, self.ground_group, False, False) or \
            (self.bird.rect.top <= 0):
            self.game_status.set_game_over()
       