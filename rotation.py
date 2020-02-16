#this code will rotate a image in specified angle

import numpy as np 
import cv2 

pic = cv2.imread("face.png")

rows = pic.shape[1]
columns = pic.shape[0]

center = (columns/2,rows/2)

angle = 180

#getRotationMatrix2D(centerofImage,AngleToRotate, scale_param)
m = cv2.getRotationMatrix2D(center, angle, 2)

rotate = cv2.warpAffine(pic, m, (columns,rows))
cv2.imshow("Rotated Image", rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
