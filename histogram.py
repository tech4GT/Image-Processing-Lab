import cv2
import numpy as np
from matplotlib import pyplot as plt


ip = cv2.imread("./Images/contrast.jpg")
img = np.zeros((ip.shape[0], ip.shape[1], 1), np.uint8)

for i in range(ip.shape[0]):
    for j in range(ip.shape[1]):
        img.itemset((i, j, 0), 0.3*ip.item(i, j, 2) +
                    0.59*ip.item(i, j, 1) +
                    0.11*ip.item(i, j, 0))

""" Inbuilt Method """
# histr = cv2.calcHist([img], [0], None, [256], [0, 256])

""" My method """
vals = np.zeros((256), np.uint8)
for i in range(ip.shape[0]):
    for j in range(ip.shape[1]):
        vals[ip.item(i, j, 0)] += 1

plt.plot(range(0, 256), vals)
plt.show()
