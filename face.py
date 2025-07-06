# importing the opencv library
import cv2
# loading the cv file
a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# giving access to camera
b = cv2.VideoCapture(0)
# loop to detecting the face and show it within the mentioned shape
while True:
    c_rec,d_image = b.read()
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    f = a.detectMultiScale(e, 1.3,6)
    for (x1,y1,w1,h1) in f:
        cv2.rectangle(d_image, (x1,y1), (x1+w1, y1+h1), (255,0,0), 5)    
    cv2.imshow('Face Detection - Press Q to Quit', d_image)

    h = cv2.waitKey(1) & 0xFF  
    if h==ord('q'):
        break
b.release()
cv2.destroyAllWindows()          