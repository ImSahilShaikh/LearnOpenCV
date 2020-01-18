import cv2

#VideoCapture method takes input device parameter as source fro video input
#default camera is generally 0 or -1
#instead 0 or device number we can pass video name.extension to read from video file
capture = cv2.VideoCapture(0);
#isOpened() method with capture variable return true if device is available or proper or filepath is correct else false

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#VideoWriter takes argument 1: name of output file 2: fourcc code i.e codec 3:fps 4:size (in tuple)
output = cv2.VideoWriter("myoutput.avi",fourcc,10.0,(640,480))

#capture frames in loop
while(True):
    #ret stores the value true if frame is available
    #frame will store captured frames
    ret, frame = capture.read()
    if ret==True:

        #videowriter instance writes the output to output file instace
        output.write(frame)

        #convert frame bgr to gray into variabl gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("First video",gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
#release all resources which captures video
capture.release()
cv2.destroyAllWindows()