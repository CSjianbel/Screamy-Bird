import pygame
import random

from game.entities.ground import Ground
from game.entities.background import Background
from game.entities.bird import Bird
from game.entities.pipe import Pipe
from game.entities.score import Score
from game.entities.leaderboard import LeaderBoard
from game.entities.end_game import GameEnd

from game.controller import GameController
from game.utils.particle import RainbowParticles


class GameManager:
    def __init__(self, config, game_status):
        self.config = config
        self.screen = self.config.screen
        self.sprites = self.config.sprites
        self.pipe_frequency = 1500
        self.last_pipe = pygame.time.get_ticks() - self.pipe_frequency
        self.game_status = game_status
        self.bird_group = pygame.sprite.Group()
        # modify
        self.pipe_group = pygame.sprite.Group()

        self.ground_group = pygame.sprite.Group()
        self.bird = Bird(self.sprites.bird, 100, int(self.config.window.height / 2), self.game_status)
        self.ground = Ground(self.sprites.ground, 300, 768, self.game_status)
        self.background = Background(self.sprites.background)
        self.score = Score(self.bird_group, self.pipe_group)
        self.pass_pipe = False
        self.ground_group.add(self.ground)
        self.bird_group.add(self.bird)
        self.rainbow_particles = RainbowParticles()
        self.game_controller = GameController(self, self.game_status)

        self.show_leaderboard = False
        self.show_result = True
        self.leaderboard = LeaderBoard(self.config, self.game_status, self.score, self)
        self.game_end = GameEnd(self.config, self.game_status, self.score, self.leaderboard, self)
        # classic, coop, xcoop
        self.game_mode = 'classic'
        # keyboard, voice, nose
        self.control_mode = 'keyboard'

    def update(self):
        self.background.draw(self.screen)
        self.rainbow_particles.draw(self.screen, self.bird.getPosY())
        self.pipe_group.draw(self.screen)

        # Get keys pressed
        keys = pygame.key.get_pressed()
        # 1,2,3 - classic, coop, xcoop
        # 8,9,0 - keyboard, voice, nose
        if self.game_status.is_game_idle:
            if keys[pygame.K_1]:
                self.game_mode = 'classic'
            elif keys[pygame.K_2]:
                self.game_mode = 'coop'
            elif keys[pygame.K_3]:
                self.game_mode = 'xcoop'
            elif keys[pygame.K_8]:
                self.control_mode = 'keyboard'
            elif keys[pygame.K_9]:
                self.control_mode = 'voice'
            elif keys[pygame.K_0]:
                self.control_mode = 'nose'

        # Standard
        self.bird_group.draw(self.screen)
        self.bird_group.update()

        if self.game_status.is_game_idle:
            self.screen.blit(self.sprites.get_ready, (159, 150))

        if self.game_status.is_game_started:
            self.score.draw(self.screen)
            self.score.update()
            self.generate_pipes()
            self.check_collisions()

        self.ground_group.draw(self.screen)
        self.ground_group.update()

        if self.game_status.is_game_over:
            if self.show_result:
                self.game_end.draw(self.screen)
                self.game_end.update()
            if self.show_leaderboard:
                self.leaderboard.draw(self.screen)
                self.leaderboard.update()
        # endstandard

        if self.game_mode == 'coop':
            self.move_pipes()
            if keys[pygame.K_p]:
                if len(self.pipe_group) != 0:
                    self.pipe_group.sprites()[-1].stop_moving()
                    self.pipe_group.sprites()[-2].stop_moving()


    def generate_pipes(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_pipe > self.pipe_frequency:
            pipe_height = random.randint(-100, 100)
            y_speed = random.randint(1, 15)
            direction = 1 if random.random() < 0.5 else -1
            btm_pipe = Pipe(self.sprites.pipe, self.config.window.width, int(self.config.window.height / 2) + pipe_height, -1, y_speed, direction)
            top_pipe = Pipe(self.sprites.pipe, self.config.window.width, int(self.config.window.height / 2) + pipe_height, 1, y_speed, direction)
            self.pipe_group.add(btm_pipe)
            self.pipe_group.add(top_pipe)
            self.last_pipe = time_now
        self.pipe_group.update()

    def move_pipes(self):
        for pipe in self.pipe_group:
            pipe.move()

    def check_collisions(self):
        if  pygame.sprite.groupcollide(self.bird_group, self.pipe_group, False, False) or \
            pygame.sprite.groupcollide(self.bird_group, self.ground_group, False, False) or \
            (self.bird.rect.top <= 0):
            self.game_status.set_game_over()

    def restart_game(self):
        self.game_status.set_game_idle()
        self.pipe_group.empty()
        self.bird.reset()
        self.score.reset()
        self.game_controller.start_voice_recognition()
       
