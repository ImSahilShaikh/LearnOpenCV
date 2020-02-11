import numpy as np 
import cv2

pic = cv2.imread("face.png")
cols = pic.shape[1]
rows = pic.shape[0]

#the array shows [x,y,value]
#if value is negative image shifts towards left side and towards right if value is positive
shift = np.float32([[1,0,-100],[0,1,-50]])

#warpAffine function takes parameters as 
#warpAffine(image,shiftArray,(columns,rows))
shifted = cv2.warpAffine(pic,shift,(cols,rows))
cv2.imshow("Shifted Image",shifted)

cv2.waitKey(0)
cv2.DestroyAllWindows()
