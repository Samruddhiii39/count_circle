
import numpy as np
import cv2



img = cv2.imread("coin3.jpg")


grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grey, (17, 17), 0)


cv2.imshow("grey scale", grey)
cv2.imshow("blurred", blurred)
cv2.waitKey(0)


outline = cv2.Canny(blurred, 30, 150)


cv2.imshow("The edges", outline)
cv2.waitKey(0)


(cnts, _) = cv2.findContours(outline, cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Result", img)
cv2.waitKey(0)



print("I found %i coins" % len(cnts)) 
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grey, (17, 17), 0)



cv2.imshow("grey scale", grey)
cv2.imshow("blurred", blurred)
cv2.waitKey(0)



outline = cv2.Canny(blurred, 30, 150)


cv2.imshow("The edges", outline)
cv2.waitKey(0)


(cnts, _) = cv2.findContours(outline, cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Result", img)
cv2.waitKey(0)


print("I found %i coins" % len(cnts))