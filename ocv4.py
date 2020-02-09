import numpy as np 
import cv2

#create a black background with unsigned int datatype of 500x500 pixels with 3 channeles(bgr)
img = np.zeros((500,500,3), dtype='uint8')

#this will create a white background
img.fill(255)

#line drawing function
cv2.line(img,(200,200),(350,350),(0,0,255))

#circle drawing function
cv2.circle(img,(250,250),50,(250,0,0))

font = cv2.FONT_HERSHEY_DUPLEX
#text printing
cv2.putText(img,"Sahil",(100,100),font,3,(0,0,0),4,cv2.LINE_8)


cv2.imshow('Dark_Pic_Created_in_Numpy',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
