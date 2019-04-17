import numpy as np
import cv2
import dilation as d
import erosion as e

ip = cv2.imread("./Images/dilation.png")
img = np.zeros((ip.shape[0], ip.shape[1], 1), np.uint8)

for i in range(ip.shape[0]):
    for j in range(ip.shape[1]):
        img.itemset((i, j, 0), 0.3*ip.item(i, j, 2) +
                    0.59*ip.item(i, j, 1) +
                    0.11*ip.item(i, j, 0))
        binIntensity = 0
        if img.item(i, j, 0) > 50:
            binIntensity = 255
        img.itemset((i, j, 0), binIntensity)

ip = np.copy(img)

se = [(-1, -1), (1, -1), (-1, 1), (1, 1), (-1, 0), (0, -1),
      (0, 0), (0, 1), (1, 0), (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2)]

inter = d.dilate(img, se)
img = e.erode(inter, se)
cv2.imshow('input', ip)
cv2.imshow('intermediate', inter)
cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
