# pyrefly: ignore [missing-import]
import cv2 

video_path = "/Users/purushothamanvenkatachalam/Downloads/Ml_project/Ho Chi Minh City Traffic Intersection Vietnam.mov"
cap= cv2.VideoCapture(video_path)

print("we are loading the video stream from the{video_path}")

while cap.isOpened():
    ret,frame= cap.read()

    # if the video ends or cannot read we need to break the loop 
    if not ret:
        print("stream ended or camera not opened ")
        break
    

    #Phase1 to convert the bgr matrix to a simple grayscale matrix - why to reduce the computational load by 3x 
    gray_frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # applying gausian blur 
    blurred_frame=cv2.GaussianBlur(gray_frame,(5,5),0)

    # apply canny edge 
    edges= cv2.Canny(blurred_frame,50,150)


    # dislay both the original and the processed onea 
    cv2.imshow('original frame',frame)
    cv2.imshow('gray scale processing layer ',edges)

    #Force the windows apart 
    cv2.moveWindow('original frame',100,100)
    cv2.moveWindow('gray scale processing layer',100,100)

    
    #to make the script eun until you use Q key 
    if cv2.waitKey(38) & 0xFF == ord('q'):
        print("manual shut down ")
        break

cap.release()
cv2.destroyAllWindows()



