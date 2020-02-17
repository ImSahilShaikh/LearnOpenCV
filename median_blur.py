import cv2

pic = cv2.imread("face.png")

#medianBlur(src,ksize i.e blur param)
#ksize should be positive odd integer
median = cv2.medianBlur(pic,9)

cv2.imshow("MedianBlur", median)

cv2.waitKey(0)
cv2.destroyAllWindows()
