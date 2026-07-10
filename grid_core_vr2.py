# pyrefly: ignore [missing-import]
import cv2 

# capturing the video 
video_path = "/Users/purushothamanvenkatachalam/Downloads/Ml_project/Ho Chi Minh City Traffic Intersection Vietnam.mov"
cd = cv2.VideoCapture(video_path)

print("We are straming from the {video_path}")

while cd.isOpened():
    # ret is status , frame is matrix of image 
    ret,frame=cd.read()

    # is stream ended 
    if not ret :
        print("stream has ended ")
        break 
    # apply grayScale  to reduce 3x of computations (3d to 2d)
    gray_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # apply gausian blur
    blurred