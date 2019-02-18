import cv2
import numpy as np
import math

img = cv2.imread('/Users/tech4GT/Desktop/Images/photo.jpeg')

# get the factor by which to shrink
c = int(input("\nEnter the factor by which to shrink\n"))

# create the output image
op = np.zeros((math.floor(img.shape[0]/c),
               math.floor(img.shape[1]/c), 3), np.uint8)

for x in range(op.shape[0]):
    for y in range(op.shape[1]):
        for channel in range(3):
            val = img.item(c*x, c*y, channel)
            # for i in range(c*x, c*x + c):
            #     for j in range(c*y, c*y + c):
            #         val += img.item(i, j, channel)
            # val = round(val/(c*c))
            # print(val)
            op.itemset((x, y, channel), val)

cv2.imshow('image', op)
cv2.waitKey(0)
cv2.destroyAllWindows()
