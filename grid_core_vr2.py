# pyrefly: ignore [missing-import]
import cv2 
# pyrefly: ignore [missing-import]
import numpy as np

# pyrefly: ignore [missing-import]
from sort import Sort 
# initilizing the tracker 
tracker= Sort(max_age=1,min_hits=3,iou_threshold=.3)

# capturing the video 
video_path = "/Users/purushothamanvenkatachalam/Documents/Ml_project/Traffic video /Karwan Bazar Pedestrians.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    # ret is status , frame is matrix of image 
    ret,frame=cap.read()

    # is stream ended 
    if not ret :
        print("stream has ended ")
        break 
    #preprocessing 
    # cropping the top portion of the video fo unnessary detailes like sky, birds etc won't be detected 
    height , width =frame.shape[:2]
    #how much to cut from the top 
    roi_start_y = int(height*.25)
    cropped_frame=frame[roi_start_y:height,0:width]

    #getting the height and width of the cropped video 
    crop_h,crop_w=cropped_frame.shape[:2]
    # apply grayScale  to reduce 3x of computations (3d to 2d)
    gray_scale=cv2.cvtColor(cropped_frame,cv2.COLOR_BGR2GRAY)
    # apply gausian blur
    blured=cv2.GaussianBlur(gray_scale,(5,5),0)
    # apply canny edge degtection
    edges=cv2.Canny(blured,50,150)

    # Creating a empty list to store the frame's detections 
    detections = []
    # gives me shape(contours-points) of edge detected images 
    contours , _ = cv2.findContours(edges,cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours :
        if cv2.contourArea(contour)>500:
            x,y,w,h=cv2.boundingRect(contour)

            x1= x
            y1=y+roi_start_y
            x2=x+w
            y2=y+roi_start_y+h
            
            detections.append([x1,y1,x2,y2,1])
    if len(detections)==0:
        detections_array=np.empty((0,5))
    else:
        detections_array=np.array(detections)
    tracked_objects=tracker.update(detections_array)

    # draw a reactangle box to the points given here 
    for track in tracked_objects:
        tx1,ty1,tx2,ty2,track_id=track
        tx1,ty1,tx2,ty2,track_id=int(tx1),int(ty1),int(tx2),int(ty2),int(track_id)
        cv2.rectangle(frame,(tx1,ty1),(tx2,ty2),(0,255,0),2)
        # drawing id above  the boxes 
        cv2.putText(frame,f"ID{track_id}",(tx1,ty1-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)

    

    # to display the output of the original and the processed ones 
    cv2.imshow('original frame - Sort tracking ',frame)
    cv2.imshow('Grayscale processed one ',edges)

    

    # a key to immedeate termination of the program 
    if cv2.waitKey(30) & 0xFF == ord('q'):
        print("shutdown requested")
        break 

cap.release()
cv2.destroyAllWindows()


