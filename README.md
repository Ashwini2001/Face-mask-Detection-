# Face-mask-Detection-
Face mask detection on raspberry pi using the HaarCascade Classifiers provided by opencv
using the haarCascade classifiers like haarcascade_frontalface_default.xml and haarcascade_mcs_mouth.xml to detect face and mouth we can easily detect if the person infront 
of the camera is wearing a face mask or not.

Used libraries:
1. OpenCV
2. Imutils

Used files for face detection:
1. haarcascade_frontalface_default.xml
2. haarcascade_mcs_mouth.xml
(Above files can be easily found in the openCV pkg in opencv/data/haarcascades/  or else you can download the files from this repository)


Summary of the code:
Video captured is accessed frame by frame and face is detected using haarcascade_frontalface_default cascade, then for every face detected mouth is detected by using
haarcascade_mcs_mouth. If mouth is detected for the respective face then a message is displayed as warning to wear a mask, else mask is detcted on the face.
