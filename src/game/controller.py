import pygame
import pyaudio
import numpy as np
import threading

class GameController:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.game_status = game_manager.game_status
        self.bird = self.game_manager.bird
        self.jump_pressed = False
        self.dash_pressed = False
        self.py_audio = pyaudio.PyAudio()
        self.scream_threshold = 0.2
        self.voice_process = None
        self.terminate_voice_process = False
        self.exit = False
        self.stream = self.py_audio.open(format = pyaudio.paFloat32,
                                         channels = 1,
                                         rate = 44100,
                                         input = True,
                                         frames_per_buffer = 1024)
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_status.set_game_over()
                #self.stop_voice_recognition()
                self.stream.stop_stream()
                self.stream.close()
                self.py_audio.terminate()
                self.exit = True

            if not self.game_status.is_game_over:
                self.jump_button_control(event)

            # if self.game_status.is_game_over:
            #     self.stop_voice_recognition()

    def jump_button_control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'l':
                if len(self.game_manager.pipes) > 1:
                    pipe1 = self.game_manager.pipes[-1]
                    pipe2 = self.game_manager.pipes[-2]
                    if (pipe1.can_close and pipe2.can_close):
                        pipe1.closePipe()
                        pipe2.closePipe()
                    # self.game_manager.pipes[0].closePipe()
                    # self.game_manager.pipes[1].closePipe()
            if event.unicode == 'a' and not self.jump_pressed:
                self.bird.jump()
                self.jump_pressed = True
            if event.unicode == 'd' and not self.dash_pressed:
                for pipe in self.game_manager.pipes:
                    pipe.fasterPipes()    
                self.dash_pressed = True
        
        if event.type == pygame.KEYUP:
            if event.unicode == 'a':
                self.jump_pressed = False
            if event.unicode == 'd':
                self.dash_pressed = False

        # if event.type == pygame.MOUSEBUTTONDOWN and not self.mouse_button_pressed:
        #     if event.button == 1:
        #         self.bird.jump()
        #         self.mouse_button_pressed = True

        # if event.type == pygame.MOUSEBUTTONUP:
        #     if event.button == 1:
        #         self.mouse_button_pressed = False

    # def start_voice_recognition(self):
    #     self.voice_process = threading.Thread(target = self.jump_voice_control)
    #     self.voice_process.start()

    # def stop_voice_recognition(self):
    #     if self.voice_process and self.voice_process.is_alive():
    #         self.terminate_voice_process = True
        
    # def jump_voice_control(self):
    #     while not self.game_status.is_game_over:
    #         # Capture audio for voice control
    #         audio_data = np.frombuffer(self.stream.read(1024), dtype=np.float32)
    #         loudness = np.abs(audio_data).mean()

    #         print(f'Loudness: {loudness}')

    #         if not self.game_status.is_game_over:
    #             if loudness > self.scream_threshold:
    #                 self.bird.jump()
            
    #         if self.terminate_voice_process:
    #             break