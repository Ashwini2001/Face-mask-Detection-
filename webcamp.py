'''Face Detection using HaarCascade'''

from  imutils.video import VideoStream
import datetime
import imutils
import time
import cv2
import requests
import RPi.GPIO as gpio

# Start video
vs = VideoStream(0).start()
time.sleep(2.0)
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

# Font for text on image
font = cv2.FONT_HERSHEY_SIMPLEX

# Load Haar Classifiers for face and mouth detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

while True:
	# Read frame by frame
    frame = vs.read()

    # Covert to grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Define waitKey
    key = cv2.waitKey(1) & 0xFF

    # Detect faces using classifier
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, 
                                 minNeighbors=4, 
                                 minSize=(30, 30))

    # If face not found
    if(len(faces) == 0):

    	# Write face not found on the image
        cv2.putText(frame,'Face not found.', (100,100), font, 1, (255,255,255), 2, cv2.LINE_AA)
    else:

    	# For every face detected
        for (x, y, w, h) in faces:

        	# Draw a rectangle over the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Detect if mask is wore by detecting mouth for selected face
            covered_faces = mouth_cascade.detectMultiScale(gray, 1.5, 5)

            # If covered
            if(len(covered_faces) == 0):

            	# Message displayed on rectangle drawn
                cv2.putText(frame,'Thanks for wearing mask', (x-10,y-10), font, 1, (255,255,0), 2, cv2.LINE_AA)
            else:

            	# Message displayed on rectangle drawn
                cv2.putText(frame,'Please wear a mask', (x-20,y-35), font, 1, (0,0,255), 2, cv2.LINE_AA)
        
        # Show the respective frame
        cv2.imshow("Feed",frame)

    # Press q to exit the loop
    if key == ord("q"):
        break

# Stop video
vs.stop()

# Destroy the windows created
cv2.destroyAllWindows()
