import numpy as np
import cv2

# img1 = np.zeros((256, 256, 1), np.uint8)
img1 = np.array([[255, 255, 255, 0], [255, 255, 255, 0], [
    255, 255, 255, 0], [0, 0, 0, 0]], dtype=np.uint8).reshape(4, 4, 1)
img2 = np.array([[0, 0, 0, 0], [0, 255, 255, 255], [
    0, 255, 255, 255], [0, 255, 255, 255]], dtype=np.uint8).reshape(4, 4, 1)

cv2.imshow('input1', img1)
cv2.imshow('input2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

for x in range(img1.shape[0]):
    for y in range(img1.shape[1]):
        img1.itemset((x, y, 0), img1.item(x, y, 0) | img2.item(x, y, 0))

cv2.imshow('output', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
