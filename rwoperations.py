#importing opencv library
import cv2
#printing version of opencv
print("version of open cv is: ",cv2.__version__ )
#imread method is used to read the image which is passed as first parameter and second parameter is flag
#flag defines in which way you want to read the image i.e color(1), grayscale(0) or with alpha channels(-1)
img=cv2.imread("face.png",-1)
#printing the value of img variable to know status of imread method
print(img)
#imshow method is used to display the image which is readed already
#first parameter is name of the window and second parameter is the variable which contains the image
cv2.imshow("First OpenCV demo",img)
#wait key method is used to define the interval of window appearance
#0 parameter will let you close the window manually
k=cv2.waitKey(0)
if k==27:
#destoryAllWindows method is used to destroy all the windows
    cv2.destroyAllWindows()
#imwrite method is used to write the image into a file
#ord is predefined method which takes key name as parameter
elif k==ord("s"):

    cv2.imwrite("face_copy.jpg",img)
