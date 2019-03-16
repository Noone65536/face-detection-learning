import cv2
#imagePath = "image.jpg" # 图片源路径
videoPath = "E://FFOutput//testvideo.avi" # 视频源路径
casePath = "C://users//edwar//downloads//haarcascade_frontalface_alt.xml" #训练数据路径
#videoCapture = cv2.VideoCapture(0)  #open the camera of the computer
faceCascade = cv2.CascadeClassifier(casePath) #导入训练数据
#image= cv2.imread(imagePath) #将图像读取到内存
video_Capture = cv2.VideoCapture(videoPath) #导入视频到vedioCapture
fps = video_Capture.get(cv2.CAP_PROP_FPS)
size = (int(video_Capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video_Capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    '"E://FFOutput//aaa6.avi"',cv2.VideoWriter_fourcc('X','V','I','D'), fps, size
)

#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # 将图像转化为灰度图
while True:
    ret, frame = video_Capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.4,  # 1.1——1.4，越高越快但容易漏检 
        minNeighbors=3,  # 最小邻居， 增加可以过滤误检对象，减少可以增加到检测对象的几率
        minSize=(10, 10)  # 检测对象的最小尺寸
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Video',frame)
    videoWriter.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cv2.waitKey(0)