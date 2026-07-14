# Read me

# The co-ordinate system in a computer works like this

where  in (x,y )

- x lowest values is 0
- but in y lowest is length of the height


<img width="1132" height="1254" alt="image" src="https://github.com/user-attachments/assets/5cb69d0c-2628-4cac-a0b0-f8407768da17" />


- to a compute a image is  in the form of matrixes  0 is pith black and 255 is white

## Phase 1 Feature extraction (what i understood initial going less powerfull canny edge after i understand that then i will go for the more powerfull model yolo )

1. Frame -  colour format ins the form of bgr , has 3 channels and full resolution 
2. then roi crop → basically slicing out 25% of the Frame 
3. next what i did was Masking - poly_frame - so it blacks out every thing outside of the sidewalk and street and only focus on the road 
    1. here what learned was that computer applies a rule to every pixel kindof
        1. even - odd rule where a ray of x→infinity and y→contant and the polygonal points we give its tested in such a way if the points intersect the ray 1 or odd  times then the point is inside the fence 
        2. if it touches it 2 or even times then goes in and come out 
    2. but this can’t be applies to every pixel at it slows down the process and uses alot of the computer process so we Scaline Algorithm 
        1. here we do it row by row (y) and find exactly where the intersection happens  
        2. then sort those intersection x-co ordinate from left to right 
        3. finally fill all the pixels b/w
    
    4. then dimensionality reductions : grayscalling ( dropping from 3 channel to 1 to save computation power - more specifically so that the canny edge can. handle 
    
    1. then noise reduction → Gaussian blurring (avg out pixels to  soften image)
        1. here what i understood was that the computer detects static motions which is basically the noise 
        2. even if human eyes tells us that the road is perfect but to  canny edge which basically depends on the change in light  so various static jitter  will be detected 
        3. thus it will identify even those noise as a object just inorder to reduce the edges but keep the contract and strong edges intact (eg cars and humans here ) we use gaussian blurring 
    
    5. finally the feature predictions edges here we use the canny but i has. various limitations i need to check those limitations and break my code to further improve my code
