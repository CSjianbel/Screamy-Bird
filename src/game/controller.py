import pygame

from .utils.audio import Audio

class GameController:
    def __init__(self, game_manager, game_status):
        self.game_manager = game_manager
        self.game_status = game_status
        self.bird = self.game_manager.bird
        self.mouse_button_pressed = False
        self.exit = False
        self.audio_recog = Audio(self.bird, game_status)
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_status.set_game_over()
                self.exit = True
                self.audio_recog.exit()

            if not self.game_status.is_game_over:
                self.jump_button_control(event)

            if self.game_status.is_game_over:
                self.stop_voice_recognition()

    def jump_button_control(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.mouse_button_pressed:
            if event.button == 1:
                self.bird.jump()
                self.mouse_button_pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.mouse_button_pressed = False

    def start_voice_recognition(self):
        self.audio_recog.start_voice_recognition()

    def stop_voice_recognition(self):
        self.audio_recog.stop_voice_recognition()

    