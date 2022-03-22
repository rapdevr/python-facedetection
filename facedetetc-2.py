from operator import truediv
import time
from turtle import speed
import cv2
import numpy as np
from playsound import playsound
import webbrowser

calibration = 0
##haarscascades were used as a pre-made facial structure template
cap = cv2.VideoCapture('STREAM URL')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print("\ncamera angle is prob ok so continuing plus i can't be bothered to code a script to do that")

detection = 1

def face_detection():
    global detection
    print("\nready to detect faces!")
    while detection == True:

        ret, frame = cap.read()

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #faces = face_cascade.detectMultiScale(gray, 1.05, 2)
        faces = face_cascade.detectMultiScale(frame, 3, 2)
        for (x, y, w, h) in faces:

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            #roi_gray = gray[y:y+w, x:x+w]
            roi_frame = frame[y:y+w, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            print("\nFace Detected!")
            detection = 0
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    #playsound('/Users/rishi/Documents/coding/bday attempt/Happy Birthday - Stevie Wonder.mp3')
    webbrowser.open("https://www.youtube.com/watch?v=o-YBDTqX_ZU")

face_detection()


