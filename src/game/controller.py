import pygame
import random
import pyaudio
import numpy as np

class GameController:
    def __init__(self, game_state, game_status):
        self.game_state = game_state
        self.game_status = game_status
        self.bird = self.game_state.bird
        self.mouse_button_pressed = False
        self.py_audio = pyaudio.PyAudio()
        self.scream_threshold = 0.2
        self.stream = self.py_audio.open(format = pyaudio.paFloat32,
                                         channels = 1,
                                         rate = 44100,
                                         input = True,
                                         frames_per_buffer = 1024)
        
    def update(self):
        self.jump_voice_control()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.is_game_over = True
                pygame.quit()

            if not self.game_status.is_game_over:
                self.jump_button_control(event)

            if self.game_status.is_game_over:
                self.restart_game(event)

    def jump_button_control(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.mouse_button_pressed:
            if event.button == 1:
                self.bird.jump()
                self.mouse_button_pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.mouse_button_pressed = False

    def jump_voice_control(self):
        # Capture audio for voice control
        audio_data = np.frombuffer(self.stream.read(1024), dtype=np.float32)
        loudness = np.abs(audio_data).mean()

        if not self.game_status.is_game_over:
            if loudness > self.scream_threshold:
                self.bird.jump()

    def restart_game(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.game_status.set_game_idle()
                self.game_state.pipe_group.empty()
                self.game_state.bird.reset()
                self.game_state.score.reset()