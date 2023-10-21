import os

import pygame
import cv2 
import numpy as np
import threading 

CASCADE_DIR = os.path.join('..', 'cascade_files')
CASCADE_FILE = os.path.join(CASCADE_DIR, 'haarcascade_mcs_nose.xml')

class NoseDetection:

    def __init__(self, window, game_manager):
        self._nose_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_mcs_nose.xml')
        self.cam = cv2.VideoCapture(0)
        self.window = window
        self.frame_surface = None
        self.stop_detecting_nose = True
        self.process = None
        self.bird = game_manager.bird

    def start_nose_detection(self):
        self.stop_detecting_nose = False
        self.process = threading.Thread(target=self.detect_nose)
        self.process.start()

    def stop_nose_detection(self):
        if self.process and self.process.is_alive():
            self.stop_detecting_nose = True

    def detect_nose(self):
        while True:
            _, frame = self.cam.read()
            #self.set_frame_surface(frame)

            # Convert frame to grayscale image
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Find a nose in the frame
            nose_rects = self._nose_cascade.detectMultiScale(gray, 1.3, 5)
            # set the coordinates of nose_pos if a nose was detected
            for (x, y, w, h) in nose_rects:
                x_center =  self.window.width - (x + w / 2)
                y_center = y + h / 2
                self.set_nose_pos((x_center, y_center))
                break

            # If no nose was detected then set it to None
            if len(nose_rects) == 0:
                self.set_nose_pos(None)
            
            # print(self.nose_pos)
            

    def get_frame_surface(self):
        return self.frame_surface

    def set_frame_surface(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        self.frame_surface = pygame.surfarray.make_surface(frame).convert()

    # self.nose_pos can have 2 possible values
    # None: There was no nose detected
    # (x, y): Coordinates of nose that was detected
    def get_nose_pos(self):
        return self.nose_pos

    def set_nose_pos(self, pos):
        self.nose_pos = pos

        # kada pag change ng nose_pos, update din yung position ng bird
        self.bird.setPos(self.nose_pos)


        