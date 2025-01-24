import cv2 as cv
import numpy as n
import matplotlib.pyplot as m

im = cv.imread("new.jpg")

cv.imshow("image",im)
cv.waitKey(2000)

m.imshow(im)
m.show()

cv.destroyAllWindows()
