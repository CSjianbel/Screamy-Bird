import pygame
import cv2
import numpy as np

nose_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_mcs_nose.xml')

if nose_cascade.empty():
  raise IOError('Unable to load the nose cascade classifier xml file')

# Initialize Pygame
pygame.init()

# Initialize the webcam capture
cap = cv2.VideoCapture(0)

# Create a Pygame window
window_width = 640
window_height = 480
screen = pygame.display.set_mode((window_width, window_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capture a frame from the webcam
    ret, frame = cap.read()

    
    # Convert the OpenCV frame to a Pygame surface
    #frame_surface = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #frame_surface = np.rot90(frame_surface)
    #frame_surface = pygame.surfarray.make_surface(frame_surface).convert()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blit the webcam feed onto the Pygame window
    #screen.blit(frame_surface, (0, 0))

    # find noses in frame
    nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)
    # draw rectangles around noses detected
    for (x, y, w, h) in nose_rects:
        x_center = window_width - (x + w / 2) 
        y_center = y + h / 2
        print(f'Nose center: ({x_center}, {y_center})')
        pygame.draw.circle(screen, (255, 0, 0), (x_center, y_center), 5)
        break



    # Update the display
    pygame.display.update()

# Release the webcam and quit Pygame
cap.release()
pygame.quit()

