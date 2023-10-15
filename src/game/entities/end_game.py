import pygame

class GameEnd:
    def __init__(self, config, game_status, score, leaderboard):
        self.config = config
        self.game_status = game_status
        self.leaderboard = leaderboard
        self.score = score
        self.result_bg = config.sprites.result
        self.game_over_label = config.sprites.game_over
        self.restart_btn = config.sprites.restart_btn
        self.home_btn = config.sprites.home_btn
        self.show_board_btn = config.sprites.show_board_btn
        self.rank = None
    
    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.game_over_label, (151, 150))
        screen.blit(self.result_bg, (100, 275))
        screen.blit(self.restart_btn, (100, 500))
        screen.blit(self.home_btn, (100 + 126 + 11, 500))
        screen.blit(self.show_board_btn, (100 + (126 * 2) + (11 * 2), 500))

        font = pygame.font.Font("../assets/fonts/flappy-font.ttf", 48)
        show_rank = font.render(f"{self.leaderboard.get_rank(self.score.score)}", True, (205, 173, 88))
        show_score = font.render(f"{self.score.score}", True, (205, 173, 88))
        screen.blit(show_rank, (190, 340))
        screen.blit(show_score, (390, 340))
