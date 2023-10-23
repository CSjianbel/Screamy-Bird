import threading
import pyaudio
import pygame
import numpy as np

class Audio:

    def __init__(self, bird, game_status):
        self.py_audio = pyaudio.PyAudio()
        self.scream_threshold = 0.2
        self.voice_process = None
        self.terminate_voice_process = False
        self.bird = bird
        self.game_status = game_status
        self.stream = self.py_audio.open(format = pyaudio.paFloat32,
                                         channels = 1,
                                         rate = 44100,
                                         input = True,
                                         frames_per_buffer = 1024)
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
        
        if not self.game_status.is_game_over:
            self.jump_button_contgrol


    def start_voice_recognition(self):
        self.voice_process = threading.Thread(target=self.jump_voice_control)
        self.voice_process.start()
    
    def stop_voice_recognition(self):
        if self.voice_process and self.voice_process.is_alive():
            self.terminate_voice_process = True

    def jump_voice_control(self):
        while not self.game_status.is_game_over:
            # Capture audio for voice control
            audio_data = np.frombuffer(self.stream.read(1024), dtype=np.float32)
            loudness = np.abs(audio_data).mean()

            # print(f'Loudness {loudness}..')

            if not self.game_status.is_game_over:
                if loudness > self.scream_threshold:
                    self.bird.jump()
            
            if self.terminate_voice_process:
                break

    def exit(self):
        self.stop_voice_recognition()
        self.stream.stop_stream()
        self.stream.close()
        self.py_audio.terminate()