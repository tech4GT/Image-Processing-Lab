import numpy as np
import cv2

ip = cv2.imread("./Images/contrast.jpg")
img = np.zeros((ip.shape[0], ip.shape[1], 1), np.uint8)


for i in range(ip.shape[0]):
    for j in range(ip.shape[1]):
        img.itemset((i, j, 0), 0.3*ip.item(i, j, 2) +
                    0.59*ip.item(i, j, 1) +
                    0.11*ip.item(i, j, 0))

total = img.shape[0]*img.shape[1]
cdf = np.zeros((256))

# Compute histogram
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        cdf[img.item(i, j, 0)] += 1

# Compute cdf
for i in range(1, 256):
    cdf[i] += cdf[i-1]
for i in range(256):
    cdf[i] /= total

# normalize to range [0,255]
factor = 255/(np.max(cdf)-np.min(cdf))
minVal = np.min(cdf)
for i in range(256):
    cdf[i] = round(factor * (cdf[i] - minVal), 0)

# Apply operation to Image
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img.itemset((i, j, 0), cdf[img.item(i, j, 0)])

cv2.imshow('input', ip)
cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
