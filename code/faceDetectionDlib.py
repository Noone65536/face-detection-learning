import dlib
from skimage import io
import cv2


#face_pose_predictor = dlib.shape_predictor(predictor_model)


face_detector = dlib.get_frontal_face_detector()
videoPath = "E://FFOutput//testvideo.avi"
input_movie = cv2.VideoCapture(videoPath)
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
fps = input_movie.get(cv2.CAP_PROP_FPS)
size = (int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT)))
output_movie = cv2.VideoWriter('E://output889.avi',fourcc,fps,size)
frame_number = 0
while True:
    ret,frame = input_movie.read()
    frame_number +=1
    
    if not ret:
        break
    if frame_number == 300:
        break
    
    rgb_frame = frame[:,:,::-1]
    detected_faces = face_detector(frame,1)
    for faces in detected_faces:
        x1 = faces.left()
        y1 = faces.top()
        x2 = faces.right()
        y2 = faces.bottom()    
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
    output_movie.write(frame)
    #cv2.imshow('Video',frame)
input_movie.release()
cv2.destroyAllWindows()