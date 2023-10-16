import pygame

from game.utils.button import Button

class GameEnd:
    def __init__(self, config, game_status, score, leaderboard, game_manager):
        self.config = config
        self.game_status = game_status
        self.leaderboard = leaderboard
        self.score = score
        self.game_manager = game_manager
        self.result_bg = config.sprites.result
        self.game_over_label = config.sprites.game_over
        self.restart_btn = Button(100, 500, config.sprites.restart_btn)
        self.home_btn = Button(100 + 126 + 11, 500, config.sprites.home_btn)
        self.show_board_btn = Button(100 + (126 * 2) + 22, 500, config.sprites.show_board_btn)
        self.rank = None
    
    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.game_over_label, (151, 150))
        screen.blit(self.result_bg, (100, 275))
        self.restart_btn.draw(screen)
        self.home_btn.draw(screen)
        self.show_board_btn.draw(screen)

        font = pygame.font.Font("../assets/fonts/flappy-font.ttf", 48)
        show_rank = font.render(f"{self.leaderboard.get_rank(self.score.score)}", True, (205, 173, 88))
        show_score = font.render(f"{self.score.score}", True, (205, 173, 88))
        screen.blit(show_rank, (190, 340))
        screen.blit(show_score, (390, 340))

        if self.restart_btn.is_clicked():
            self.game_manager.restart_game()

        if self.home_btn.is_clicked():
            # for now the home button will just restart the game
            # but in the future this should go back to the main menu to choose other game modes
            self.game_manager.restart_game()

        if self.show_board_btn.is_clicked():
            self.game_manager.show_leaderboard = True
            self.game_manager.show_result = False