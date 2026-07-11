# pyrefly: ignore [missing-import]
import cv2 
# pyrefly: ignore [missing-import]
import numpy as np

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
    height , width =frame.shape[:2]

    #how much to cut from the top 
    roi_start_y = int(height*.25)
    cropped_frame=frame[roi_start_y:height,0:width]

    #getting the height and width of the cropped video 
    crop_h,crop_w=cropped_frame.shape[:2]

    # applying polygon mask 
    polygon_points=np.array([
        [int(crop_w*0.1),crop_h],
        [int(crop_w*.4),int(crop_h*.5)],
        [int(crop_w*.6),int(crop_h*.5)],
        [int(crop_w*.9),crop_h]
    ],np.int32)
    #reshape points for fillPoly
    polygon_points=polygon_points.reshape((-1,1,2))

    # creating a black mask exact size as the frame 
    mask= np.zeros((crop_h,crop_w),dtype=np.uint8)

    # filling the polygon area on the mask with white 
    cv2.fillPoly(mask,[polygon_points],255)
    
    # applying this to the cropped frame 
    poly_frame=cv2.bitwise_and(cropped_frame,cropped_frame,mask=mask)

    # apply grayScale  to reduce 3x of computations (3d to 2d)
    gray_scale=cv2.cvtColor(poly_frame,cv2.COLOR_BGR2GRAY)
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


