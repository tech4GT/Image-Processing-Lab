import cv2
import numpy as np
import math


# A function to get the iterm or padding item
def get(img, x, y, channel):
    if x < 0:
        x = 0
    if x >= img.shape[0]:
        x = img.shape[0]-1
    if y < 0:
        y = 0
    if y >= img.shape[1]:
        y = img.shape[1]-1

    return img.item(x, y, channel)


def convolve(img, cpy, filter, x, y, l):
    for channel in range(img.shape[2]):
        sum = 0
        fpx = 0
        fpy = 0
        for i in range(x-math.floor(l/2), (x+math.floor(l/2))+1):
            for j in range(y-math.floor(l/2), (y+math.floor(l/2))+1):
                sum += (get(cpy, i, j, channel) * filter.item(fpx, fpy, 0))
                fpy += 1
            fpx += 1
            fpy = 0

        img.itemset((x, y, channel), sum)


ip = cv2.imread("./Images/qrcode.jpg")
imgX = np.zeros((ip.shape[0], ip.shape[1], 1), np.uint8)
# imgX = np.array([[[50, 50, 10], [50, 50, 10], [50, 50, 10]]]).reshape(3, 3, 1)
for i in range(ip.shape[0]):
    for j in range(ip.shape[1]):
        imgX.itemset((i, j, 0), 0.3*ip.item(i, j, 2) +
                     0.59*ip.item(i, j, 1) +
                     0.11*ip.item(i, j, 0))

imgY = np.copy(imgX)


filter_length = 3

cv2.imshow('input', imgX)
cv2.waitKey(0)
cv2.destroyAllWindows()


filterX = np.array([[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]]).reshape(3, 3, 1)
filterY = np.array([[[-1, -2, -1], [0, 0, 0], [1, 2, 1]]]).reshape(3, 3, 1)

cpy = np.copy(imgX)

for x in range(imgX.shape[0]):
    for y in range(imgX.shape[1]):
        convolve(imgX, cpy, filterX, x, y, filter_length)

for x in range(imgY.shape[0]):
    for y in range(imgY.shape[1]):
        convolve(imgY, cpy, filterY, x, y, filter_length)

for x in range(imgY.shape[0]):
    for y in range(imgY.shape[1]):
        imgX.itemset((x, y, 0), abs(imgX.item(x, y, 0)) +
                     abs(imgY.item(x, y, 0)))

cv2.imshow('output', imgX)
cv2.waitKey(0)
cv2.destroyAllWindows()
