import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('src/data/haarcascade_frontalface_alt2.xml' )
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for(x,y,w,h) in faces:
      print(x,y,w,h)
      roi_gray = gray[y:y+h,x:x+w]
      roi_color = frame[y:y+h,x:x+w]
      img_item="sharath2.png"
      cv2.imwrite(img_item,roi_gray)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()