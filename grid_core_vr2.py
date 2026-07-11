# pyrefly: ignore [missing-import]
import cv2 

# capturing the video 
video_path = "/Users/purushothamanvenkatachalam/Downloads/Ml_project/Karwan Bazar Pedestrians.mp4"
cap = cv2.VideoCapture(video_path)

print(f"We are streaming from {video_path}")

while cap.isOpened():
    # ret is status , frame is matrix of image 
    ret,frame=cap.read()

    # is stream ended 
    if not ret :
        print("stream has ended ")
        break 
    # cropping the top portion of the video fo unnessary detailes like sky, birds etc won't be detected 
    height , width ,_=frame.shape

    #how much to cut 
    roi_start_y = int(height*.25)
    cropped_frame=frame[roi_start_y:height,0:width]

    # apply grayScale  to reduce 3x of computations (3d to 2d)
    gray_scale=cv2.cvtColor(cropped_frame,cv2.COLOR_BGR2GRAY)
    # apply gausian blur
    blured=cv2.GaussianBlur(gray_scale,(5,5),0)
    # apply canny edge degtection
    edges=cv2.Canny(blured,50,150)

    # to display the output of the original and the processed ones 
    cv2.imshow('original frame',frame)
    cv2.imshow('Grayscale processed one ',edges)

    # forcing the windos appart a mac thing 
    cv2.moveWindow('original frame',100,100)
    cv2.moveWindow('Grayscale processed one ',600,600)

    # a key to immedeate termination of the program 
    if cv2.waitKey(30) & 0xFF == ord('q'):
        print("shutdown requested")
        break 

cap.release()
cv2.destroyAllWindows()


