#code for gaussian blur

import cv2
import numpy as np

pic = cv2.imread("face.png")

matrix = (7,7)

#GaussianBlur(src,ksize,sigmax i.e std deviation in x)
blur = cv2.GaussianBlur(pic,matrix,0)

cv2.imshow("GaussianBlur Example", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
