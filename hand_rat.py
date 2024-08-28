import cv2
import time
import pyautogui 
import mediapipe as mp
cam = cv2.VideoCapture(0)
han_d= mp.solutions.hands.Hands()
draw_u = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()
x_index=0
y_index=0
while True:
    rev, fram = cam.read()
    fram= cv2.flip(fram,1)
    fram_h , fram_w, _ =fram.shape
    rgb_fram= cv2.cvtColor(fram,cv2.COLOR_BGR2RGB)
    out = han_d.process(rgb_fram)
    hands= out.multi_hand_landmarks
    if hands:
        for hand in hands:
            draw_u.draw_landmarks(fram,hand)
            landmarks= hand.landmark
            for id, landmark in enumerate( landmarks):
                x = int(landmark.x* fram_w)
                y = int(landmark.y*fram_h)
                if id==8:
                   
                    cv2.circle(fram,(x,y),10,(0,255,255))
                    y_index = screen_h / fram_h*y
                    x_index = screen_w / fram_w*x
                    pyautogui.moveTo(x_index,y_index)
                if id==4:
                  
                    cv2.circle(fram,(x,y),10,(0,255,255))
                    y_thum = screen_h / fram_h*y
                    x_thum = screen_w / fram_w*x
                   
                    if abs(y_index-y_thum) < 20 :
                        pyautogui.click()
                        time.sleep(1)
    cv2.imshow('fram',fram)
    cv2.waitKey(1)
