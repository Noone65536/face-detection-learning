# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:00:44 2019

@author: Edwar
"""

import face_recognition
import cv2
videoPath = "E://FFOutput//testvideo2.avi"
input_movie = cv2.VideoCapture(videoPath)
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
fps = input_movie.get(cv2.CAP_PROP_FPS)
size = (int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT)))
output_movie = cv2.VideoWriter('E://succeed3355555.avi',fourcc,fps,size)
frame_number = 0
while True:
    ret,frame = input_movie.read()
    frame_number +=1
    print("the %d frame", frame_number)
    
    if not ret:
        break
    
    if frame_number == 1000:
        break
   
    
    rgb_frame = frame[:,:,::-1]
    print("processing")
    face_locations = face_recognition.face_locations(rgb_frame,number_of_times_to_upsample=3,model='hog')
    for(top,right,bottom,left) in face_locations:
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
    print("writing")
    output_movie.write(frame)
    #cv2.imshow('Video',frame)
input_movie.release()
cv2.destroyAllWindows()