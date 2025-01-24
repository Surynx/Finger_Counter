import cv2 as cv

image = cv.imread("bird.jpg",0) #0 for making it b/w

cv.imshow("image",image)


cv.waitKey(4000)
cv.imwrite("new.jpg",image)
cv.destroyAllWindows()

