#Code for Canny Edge detection
import cv2

pic = cv2.imread("face.png")

threshold_val_1 = 60
threshold_val_2 = 150

#Canny takes three arguments
#lower threshold and upper threshold are most important parameters to understand how it works
canny = cv2.Canny(pic, threshold_val_1, threshold_val_2)

cv2.imshow("Canny edge detection",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()