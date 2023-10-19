import cv2
import numpy as np

nose_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_mcs_nose.xml')

if nose_cascade.empty():
  raise IOError('Unable to load the nose cascade classifier xml file')

# Initialize video capture using webcam
cap = cv2.VideoCapture(0)
ds_factor = 0.5

while True:
    # Read from the camerra
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # find noses in frame
    nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)
    # draw rectangles around noses detected
    for (x, y, w, h) in nose_rects:
        print(f'Nose center: ({x + w / 2}, {y + h / 2})')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        break


    cv2.imshow('Nose Detector', frame)

    # Press esc to exit 
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()