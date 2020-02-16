#code to do image thresholding

import cv2

pic = cv2.imread("face.png",0)

#threshold(src,threshold_value,max_value(i.e 255(white)),type_of_threshold)
(T_value,binary_threshold) = cv2.threshold(pic,100,255,cv2.THRESH_BINARY_INV)

cv2.imshow("Binary threshold",binary_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
