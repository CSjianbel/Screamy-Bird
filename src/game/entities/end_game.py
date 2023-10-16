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
        self.name_input = config.sprites.name_input
        self.name_input_placeholder = config.sprites.name_input_placeholder
        self.submit_btn = Button(383, 410, config.sprites.submit_btn)
        self.show_board_btn = Button(100 + (126 * 2) + 22, 500, config.sprites.show_board_btn)
        self.username = ''
        self.rank = None
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.username = self.username[:-1]
                else:
                    if event.unicode.isalpha():
                        self.username += event.unicode

    def draw(self, screen):
        screen.blit(self.game_over_label, (151, 150))
        screen.blit(self.result_bg, (100, 275))

        label_font = pygame.font.Font("../assets/fonts/flappy-font.ttf", 48)
        input_font = pygame.font.Font("../assets/fonts/chary.ttf", 26)

        if not self.leaderboard.has_saved_data:
            if len(self.username) > 0:
                screen.blit(self.name_input, (133, 410))
            else:
                screen.blit(self.name_input_placeholder, (133, 410))
            
            self.submit_btn.draw(screen)
            username_input = input_font.render(f"{self.username}", True, (205, 173, 88))
            screen.blit(username_input, (144, 415))
        else:
            score_submitted_prompt = input_font.render("Score Submitted!", True, (205, 173, 88))
            screen.blit(score_submitted_prompt, (220, 419))

        self.restart_btn.draw(screen)
        self.home_btn.draw(screen)
        self.show_board_btn.draw(screen)

        show_rank = label_font.render(f"{self.leaderboard.get_rank(self.score.score)}", True, (205, 173, 88))
        show_score = label_font.render(f"{self.score.score}", True, (205, 173, 88))

        screen.blit(show_rank, (190, 340))
        screen.blit(show_score, (390, 340))

        if self.restart_btn.is_clicked():
            self.game_manager.restart_game()
            self.leaderboard.has_saved_data = False
            self.username = ''

        if self.home_btn.is_clicked():
            # for now the home button will just restart the game
            # but in the future this should go back to the main menu to choose other game modes
            self.game_manager.restart_game()
            self.leaderboard.has_saved_data = False
            self.username = ''

        if self.show_board_btn.is_clicked():
            self.game_manager.show_leaderboard = True
            self.game_manager.show_result = False

        if self.submit_btn.is_clicked() and not self.leaderboard.has_saved_data and len(self.username) > 0:
            self.leaderboard.save_data(self.username, self.score.score)
            self.leaderboard.has_saved_data = True