import pygame

from .utils.audio import Audio

class GameController:
    def __init__(self, game_manager, game_status):
        self.game_manager = game_manager
        self.game_status = game_status
        self.jump_pressed = False
        self.dash_pressed = False
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

        if self.game_manager.game_mode == 'xcoop':
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

    def start_voice_recognition(self):
        self.audio_recog.start_voice_recognition()

    def stop_voice_recognition(self):
        self.audio_recog.stop_voice_recognition()

    