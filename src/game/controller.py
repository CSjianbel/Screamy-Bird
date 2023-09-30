import pygame
import random
import pyaudio
import numpy as np
import threading

class GameController:
    def __init__(self, game_manager, game_status):
        self.game_manager = game_manager
        self.game_status = game_status
        self.bird = self.game_manager.bird
        self.mouse_button_pressed = False
        self.py_audio = pyaudio.PyAudio()
        self.scream_threshold = 0.2
        self.voice_process = None
        self.stream = self.py_audio.open(format = pyaudio.paFloat32,
                                         channels = 1,
                                         rate = 44100,
                                         input = True,
                                         frames_per_buffer = 1024)
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_manager.is_game_over = True
                self.game_status.set_game_over()
                pygame.quit()
                self.stop_voice_recognition()
                self.stream.stop_stream()
                self.stream.close()
                self.py_audio.terminate()

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

    def start_voice_recognition(self):
        self.voice_process = threading.Thread(target = self.jump_voice_control)
        self.voice_process.start()

    def stop_voice_recognition(self):
        if self.voice_process and self.voice_process.is_alive():
            self.voice_process.terminate()
        
    def jump_voice_control(self):
        while not self.game_status.is_game_over:
            # print("hello")
            # Capture audio for voice control
            audio_data = np.frombuffer(self.stream.read(1024), dtype=np.float32)
            loudness = np.abs(audio_data).mean()

            # print(loudness)

            if not self.game_status.is_game_over:
                if loudness > self.scream_threshold:
                    self.bird.jump()

    def restart_game(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.game_status.set_game_idle()
                self.game_manager.pipe_group.empty()
                self.game_manager.bird.reset()
                self.game_manager.score.reset()
                self.game_manager.leaderboard.reset_saved_data()
                self.stop_voice_recognition()
                self.start_voice_recognition()