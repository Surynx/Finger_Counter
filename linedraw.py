import cv2 as cv
import numpy as n
import matplotlib.pyplot as m


image = m.imread("wall.jpg")
m.imshow(image)
m.show()
c = cv.imread("wall.jpg")


cv.line(c,(500,99),(769,638),(255,0,0),5)
cv.rectangle(c,(534,55),(694,551),(0,255,0),5)
cv.imshow('imag',c)


cv.waitKey(0)
cv.destroyAllWindows()