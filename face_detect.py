#Face detection using haar_cascade
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

videoCapture = cv2.VideoCapture(0)

scalefactor = 1.3

while 1:
    ret, pic = videoCapture.read()

    faces = face_cascade.detectMultiScale(pic, scalefactor,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(pic,(x , y),(x+w , y+h), (0,0,255), 2)

    print("number of faces found {}",format(len(faces)))
    cv2.imshow("Face_Detection", pic)
    k = cv2.waitKey(30) & 0xff
    if k==2:
        break

cv2.destroyAllWindows()
