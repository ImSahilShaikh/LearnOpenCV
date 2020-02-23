#Following code demonstrates bilateralFilter function in openCv 
import cv2

pic = cv2.imread("face.png")

#parameters required for bilateral filtering
#dimension_pixel is diameter from center pixel to preserve from blur effect
dim_pixel = 10
#color of pixels
color = 100
#space is the distance from center for blur effect
space = 100

filter = cv2.bilateralFilter(pic,dim_pixel,color,space)

cv2.imshow("Bilateral Filtered Image",filter)
cv2.waitKey(0)
cv2.destroylAllWindows()