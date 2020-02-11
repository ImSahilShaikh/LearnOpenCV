#Functions to draw geometric shapes on images

import cv2

img = cv2.imread('face.png',-1)

#line| arrowedLine(image, start_pts, end_pts, colorBGR,thickness)
img = cv2.line(img,(0,0),(255,255),(0,0,255), 3)
img = cv2.arrowedLine(img,(255,100),(255,255),(0,255,255), 2)

#rectangle(image,x1y1,x2y2,colorBGR,thickness)
#thickness if given -1 then shape fills with given color
img = cv2.rectangle(img, (300,100), (500,300), (255,0,0), 3)

#circle(image,center,radius,colorBGR,thicknes)
#thickness if given -1 then shape fills with given color
img = cv2.circle(img, (400,200), 50, (255,255,0), 2)

#set fontface in simple words font style
font = cv2.FONT_HERSHEY_SIMPLEX

#putText(image,texttobeprinted,start_pts,fontface,fontsize,color,thickness,linetype)
img = cv2.putText(img, "SAHIL LEARNING OpenCV", (0,700), font, 3,(15,55,255),7, cv2.LINE_AA)

cv2.imshow("image",img)

k=cv2.waitKey(0)
