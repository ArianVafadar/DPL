
import cv2

faceCascade = cv2.CascadeClassifier('/home/pi/.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('/home/pi/.local/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier('/home/pi/.local/lib/python3.7/site-packages/cv2/data/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) 
cap.set(4,480) 
i = 0
while i != 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    if i==0:
        print("unable to detect face")

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eyeCascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.5,
            minNeighbors=5,
            minSize=(5, 5),
            )
        
        
        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.5,
            minNeighbors=15,
            minSize=(25, 25),
            )
        
        
        cv2.imshow('video', img)
        if len(faces)!=0 and len(eyes)==0:
            print("unable to detect eyes")
        if len(faces)!=0 and len(smile)==0:
            print("unable to detect mouth")
        if len(faces)!=0 and len(eyes)!=0 and len(smile)!=0:
            face = cv2.imwrite(filename="face.jpg", img=img)
            print("face captured")
            i = 1
            break
    cv2.imshow('video', img)
cap.release()
cv2.destroyAllWindows()
