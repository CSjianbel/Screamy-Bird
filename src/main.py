import pygame
from pygame.locals import *

from game.manager import GameManager
from game.controller import GameController

from game.utils.sprites import Sprites
from game.utils.window import Window
from game.utils.config import GameConfig
from game.utils.status import GameStatus


class FlappyBird:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()
        self.window = Window(600, 800)
        self.sprites = Sprites()
        self.fps = 60
        self.screen = pygame.display.set_mode((self.window.width, self.window.height))
        self.is_game_over = False
        self.is_game_started = False
        
    def start(self):
        game_status = GameStatus()
        game_config = GameConfig(self.screen, self.window, self.sprites, self.fps, self.clock)
        game_state = GameManager(game_config, game_status)
        game_controller = GameController(game_state, game_status)

        # create a child process for voice recognition
        game_controller.start_voice_recognition()

        while not game_controller.exit:
            self.clock.tick(self.fps)
            game_controller.update()
            game_state.update()
            
            pygame.display.update()


def main():
    flappyBirdGame = FlappyBird()
    flappyBirdGame.start()

if __name__ == "__main__":
    main()