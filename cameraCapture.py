import cv2
import numpy as np

from trainingModel import trainUser

def cameraCap():
    capture = cv2.VideoCapture(0)
    faceCap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #cascadeClassifier is a pretrained model, and the arguments are the path to the pretrained model to use
    if not capture.isOpened():
        print("Error: could not open camera")
        return
    
    try:
        with open("id.txt", "r") as file:
            id = file.readline()
        #id = int(id)
        
        count = 0

        while True:
            ret, frame = capture.read()
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converts the image (video-captured image) into grayscale

            #1.3 (2nd parameter) is the scale factor. You must change the size of the image so that haar-cascade can compare it to. the scale factor tells how much to shrink the image to
            # next paramter (5) is the min_neighbor. it's the parameter that teels haar-cascade how many "neighbors" of potential faces to retain it
            faces = faceCap.detectMultiScale(gray, 1.4, 6) #returns the position of all the faces that is detected
            # x,y,w,h are the dimensions of the rectangle that are gonna be drawn around a face
            for (x,y,w,h) in faces:
                count += 1
                cv2.imwrite("datasets/User." + str(id) + "." + str(count) + ".jpg", gray[y:y+h, x:x+w])
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3) # draws a rectangle from the starting corner (x, y) to the end/opposite corner (x + w, y + h). And then it's just the color and thickness
            
            cv2.imshow("video", frame)
            

            if cv2.waitKey(1) == ord('q') or count > 200:
                break
    
    finally:   
        capture.release()
        cv2.destroyAllWindows()
        
    with open("id.txt", "w") as file:
            id = int(id)
            id += 1
            file.write(str(id))
    
    n = input("Enter your name: ")
    with open("names.txt", "a") as file:
        file.write(n + "\n")
    
    trainUser()
    
