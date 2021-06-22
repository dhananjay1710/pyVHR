import numpy as np
import pandas as pd
import cv2
import time


def video_cap():
    
    #Frames vars to control video capture
    capture_duration = 11
    frame_time = 10  # time of each frame in ms


    # video capture
    capture = cv2.VideoCapture(0)
    # Encoding
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Write and save
    out = cv2.VideoWriter('record.avi',fourcc, 20.0, (640,480))
    start_time = time.time()

    # Time interval
    while(int(time.time() - start_time) < capture_duration):
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)
        cv2.imwrite('./data/image.png',frame)
        cv2.imshow('Vide Capture', gray)
        if cv2.waitKey(frame_time) & 0xFF == ord('q'):
            break

    capture.release()
    out.release()
    cv2.destroyAllWindows()









if __name__ == '__main__':
    video_cap()