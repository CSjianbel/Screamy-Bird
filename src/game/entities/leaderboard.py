import json
import pygame
import pygame_textinput
from ..utils.button import Button

class LeaderBoard:
    def __init__(self, config, game_status, score, game_manager):
        self.game_manager = game_manager
        self.score = score
        self.game_status = game_status
        self.config = config
        self.leaderboard_process = None
        self.leaderboard_data = []
        self.leaderboard_bg = config.sprites.leaderboard
        self.leaderboard_table = config.sprites.leaderboard_table
        self.has_saved_data = False
        self.textinput = pygame_textinput.TextInputVisualizer()
        self.back_btn = Button(100, 75, config.sprites.back_btn)
        self.save_button = Button(280, 200, self.config.sprites.save_button)

        # events = pygame.event.get()
        # self.textinput.update(events)

        # if self.save_button.is_clicked() and not self.has_saved_data:
        #     self.has_saved_data = True
        #     self.create_data()

    def update(self):
        pass
 
    def draw(self, screen):
        self.back_btn.draw(screen)
        screen.blit(self.leaderboard_bg, (100, 150))
        screen.blit(self.leaderboard_table, (130, 230))
        #screen.blit(self.textinput.surface, (280, 100))
        #self.save_button.draw(screen)
        self.leaderboard_list(screen)

        if self.back_btn.is_clicked():
            self.game_manager.show_leaderboard = False
            self.game_manager.show_result = True


    def create_data(self, username, score):
        print("data created")
        new_data = {
            "name": username,
            "score": score
        }

        return new_data
    
    def read_data(self):
        with open("data/leaderboard.json", "r") as infile:
            self.leaderboard_data = json.load(infile)

    def save_data(self, username, score):
        new_data = self.create_data(username, score)
        self.read_data()

        self.leaderboard_data.append(new_data)
        self.leaderboard_data = sorted(self.leaderboard_data, key=lambda entry: entry['score'], reverse=True)

        with open("data/leaderboard.json", "w") as outfile:
            json.dump(self.leaderboard_data, outfile, indent=4, separators=(',', ': '))
        
        print('score saved')

    def leaderboard_list(self, screen):
        self.read_data()
        self.leaderboard_data = sorted(self.leaderboard_data, key = lambda entry: entry['score'], reverse = True)
        font = pygame.font.Font("../assets/fonts/flappy-font.ttf", 18)

        for i in range(10):
            if i < len(self.leaderboard_data):
                entry = self.leaderboard_data[i]
                rank = font.render(f"{i + 1}", True, (205, 173, 88))
                player_name = font.render(f"{entry['name']}", True, (205, 173, 88))
                score = font.render(f"{entry['score']}", True, (205, 173, 88))
            else:
                rank = font.render(f"{i + 1}", True, (205, 173, 88))
                player_name = font.render("", True, (205, 173, 88))
                score = font.render("", True, (205, 173, 88))
            
            screen.blit(rank, (146, 275 + i * 35.5))
            screen.blit(player_name, (180, 275 + i * 35.5))
            screen.blit(score, (420, 275 + i * 35.5))

    def get_rank(self, score):
        self.read_data()
        self.leaderboard_data = sorted(self.leaderboard_data, key = lambda entry: entry['score'], reverse = True)
        rank = 1

        for entry in self.leaderboard_data:
            if score < entry['score']:
                rank += 1
            else:
                break
        
        return rank
