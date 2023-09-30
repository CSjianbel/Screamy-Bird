import json
import pygame
import pygame_textinput
from ..utils.button import Button

class LeaderBoard:
    def __init__(self, config, game_status, score):
        self.score = score
        self.game_status = game_status
        self.config = config
        self.leaderboard_process = None
        self.leaderboard_data = []
        self.has_saved_data = False
        self.textinput = pygame_textinput.TextInputVisualizer()
        self.save_button = Button(280, 200, self.config.sprites.save_button)

    def update(self):
        events = pygame.event.get()
        self.textinput.update(events)

        if self.save_button.is_clicked() and not self.has_saved_data:
            self.has_saved_data = True
            self.create_data()
 
    def draw(self, screen):
        screen.blit(self.textinput.surface, (280, 100))
        self.save_button.draw(screen)

    def create_data(self):
        print("data created")
        new_data = {
            "name": self.textinput.value,
            "score": self.score.score
        }

        self.read_data()
        self.save_data(new_data)

    def save_data(self, new_data):
        self.leaderboard_data.append(new_data)
        self.leaderboard_data = sorted(self.leaderboard_data, key=lambda entry: entry['score'], reverse=True)

        with open("data/leaderboard.json", "w") as outfile:
            json.dump(self.leaderboard_data, outfile, indent=4, separators=(',', ': '))

    def read_data(self):
        with open("data/leaderboard.json", "r") as infile:
            self.leaderboard_data = json.load(infile)

    def reset_saved_data(self):
        self.has_saved_data = False

#     def get_rank(self, score):
#         # Get the rank of a player based on their score
#         self.leaderboard.sort(reverse=True, key=lambda entry: entry['score'])
#         rank = next((i + 1 for i, entry in enumerate(self.leaderboard) if entry['score'] <= score), None)
#         return rank
