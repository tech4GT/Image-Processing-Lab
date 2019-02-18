import cv2
import numpy

img = cv2.imread('./Images/photo.jpeg')
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        img.itemset((x, y, 0), 255 - img.item(x, y, 0))
        img.itemset((x, y, 1), 255 - img.item(x, y, 1))
        img.itemset((x, y, 2), 255 - img.item(x, y, 2))

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
