import numpy as np
import cv2


img = cv2.imread(r'C:\Users\acer\Desktop\img1.jpg') #enter the image path here

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray,(5,5),0);

minDist = 100
param1 = 30
param2 = 50
minRadius = 5
maxRadius = 300

# docstring of HoughCircles: HoughCircles(image, method, dp=1, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) -> circles
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

if circles is not None:
    print("Circle Detected")
    x = float(input("Enter x value:"))
    print(x)
    y = float(input("Enter y value : "))
    print(y)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        a,b,r = i[0],i[1],i[2]
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

    if ((x - a)**2 + (y - b)**2 <= r * r):
        print("The given pixel coordinates are inside the circle")
    else:
        print("The given pixel coordinates are outside the circle")
    # Show result for testing:
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
 print("circle not detected")