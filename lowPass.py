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


def convolve(img, filter, x, y, l):
    for channel in range(3):
        sum = 0
        fpx = 0
        fpy = 0
        for i in range(x-math.floor(l/2), (x+math.floor(l/2))+1):
            for j in range(y-math.floor(l/2), (y+math.floor(l/2))+1):
                sum += (get(img, i, j, channel) * filter.item(fpx, fpy, 0))
                fpy += 1
            fpx += 1
            fpy = 0

        sum = round(sum/(l*l))
        img.itemset((x, y, channel), sum)


img = cv2.imread("./Images/ironman.jpeg")


filter_length = int(input("\nPlease Enter the filter size\n"))

cv2.imshow('input', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


filter = np.zeros((filter_length, filter_length, 1), np.uint8)
filter.fill(1)

for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        convolve(img, filter, x, y, filter_length)


cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
