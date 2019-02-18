import cv2
import numpy

img = cv2.imread('./Images/photo.jpeg')
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        val = 0.11*img.item(x, y, 0) + 0.59*img.item(x,
                                                     y, 1) + 0.3*img.item(x, y, 2)
        img.itemset((x, y, 0), val)
        img.itemset((x, y, 1), val)
        img.itemset((x, y, 2), val)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
