import cv2
import numpy

img = cv2.imread('/Users/tech4GT/Desktop/Images/photo.jpeg')
it = cv2.imread('/Users/tech4GT/Desktop/Images/photo.jpeg')
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        it.itemset((x, y, 0), 0)
        it.itemset((x, y, 1), 0)
        it.itemset((x, y, 2), img.item(x, y, 2))
cv2.imshow("image", it)
cv2.waitKey(0)
cv2.destroyAllWindows()

for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        it.itemset((x, y, 0), 0)
        it.itemset((x, y, 2), 0)
        it.itemset((x, y, 1), img.item(x, y, 2))
cv2.imshow("image", it)
cv2.waitKey(0)
cv2.destroyAllWindows()

for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        it.itemset((x, y, 2), 0)
        it.itemset((x, y, 1), 0)
        it.itemset((x, y, 0), img.item(x, y, 2))
cv2.imshow("image", it)
cv2.waitKey(0)
cv2.destroyAllWindows()
