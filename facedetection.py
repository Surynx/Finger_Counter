import cv2 as cv
import numpy as nm
import matplotlib.pyplot as mt


face_rec = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
im = cv.imread("th.jpeg")

grey = cv.cvtColor(im,cv.COLOR_BGRA2GRAY)
face = face_rec.detectMultiScale(grey,1.3,4)
print(face)

for x,y,w,h in face:
    cv.rectangle(im,(x,y),(x+w,y+h),(0,255,0),5)

cv.imshow("image",im)
cv.waitKey(0)
cv.destroyAllWindows()