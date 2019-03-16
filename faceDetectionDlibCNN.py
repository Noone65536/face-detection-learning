# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:26:19 2019

@author: Edwar
"""
import cv2
import dlib
videoPath = "E://FFOutput//testvideo.avi" # 视频源路径
video_Capture = cv2.VideoCapture(videoPath) #导入视频到vedioCapture
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
fps = video_Capture.get(cv2.CAP_PROP_FPS)
size = (int(video_Capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video_Capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
output_video = cv2.VideoWriter(
    '"E://output_test1_cnnPy_1.avi"',fourcc, fps, size)
cnn_face_detector = dlib.cnn_face_detection_model_v1('D://mmod_human_face_detector.dat') 
win = dlib.image_window()
#initialize cnn based face detector with the weights
#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # 将图像转化为灰度图
frame_number = 0
while True:
    ret, frame = video_Capture.read()
    frame_number +=1
    
    print(frame_number)
    if not ret:
        break
    
    if frame_number == 30:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    print("1号位")
    faces = cnn_face_detector(gray,1)
    
    for i, d in enumerate(faces):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(
            i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), d.confidence))
        cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
#   rects = dlib.rectangles()
#   for face in faces:
#       print("3号位")
#       x = face.rect.left()
#       y = face.rect.top()
#       w = face.rect.right()
#       h = face.rect.bottom()
#       cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
#       print(xywh)

#   cv2.imshow('Video',frame)
    output_video.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_Capture.release()
cv2.destroyAllWindows()

# cv2.waitKey(0)
