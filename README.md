# circle-detection
Given an image find whether the image has a circular region and if so evaluate the given pixel is inside that circular region
The sample images are given in "circles" folder.

how I solved the problem?

I used HoughCircles function from opencv to solve this problem.first I have converted the input image to greyscale and applied some guassianblur inorder to increase the accuracy of the detected circles.Then I applied HoughCircles function to the image and adjusted the parameters for the best results.for drawing the circle I used circles function in opencv.To check whether the given pixel coordinates are inside or outside I used General Equation for a Circle: (x - h)^2 + (y - k)^2 = r^2 where (h,k) are the coordinates of the center of the circle, and r is the radius.
