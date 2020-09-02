# Template matching is searching and location a template image in the main image...

import cv2
import numpy as np

img = cv2.imread('one.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread('one_text.jpg',0)

# print(template.shape[::])    # this gives (27,71)...
width,height = template.shape[::-1] # this means we want width and column height in reverse order.

# matching the template with method "TM_CCOEFF_NORMED".
result = cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)
print(result)
# this result matrix if it contains 1 as the value that shows the brightest point.

# now we will find the point that is brightest...
threshold = 0.95
loc = np.where(result >= threshold)
print(loc)    # this pixel values are found to have the "maximum match"...

# if multiple templates are present...
# "zip" helps to "iterate" over the "loc variable".
# "zip(*loc[::-1])" asterisk(*) in this is used for 1 to 1...
# ...element matching from all the arrays that we have in a list.
for points in zip(*loc[::-1]):
    cv2.rectangle(img, points,(points[0]+width,points[1]+height),(255,98,151),2)

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()