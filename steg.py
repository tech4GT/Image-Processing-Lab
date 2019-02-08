import cv2
import numpy as np


def encode(image, msg, row):
    msg = bin(msg)[2:]
    length = bin(len(msg))[2:].zfill(8)
    for x in range(8 + len(msg)):
        val = 0
        if(x < 8):
            val = int(length[x])
        else:
            val = int(msg[x-8])
        item = img.item(row, x, 0)
        if(val == 0):
            item = item & 254
        else:
            item = item | 1
        img.itemset((row, x, 0), item)


def extract(image, row):
    rv = ""
    length = ""
    for x in range(8):
        item = img.item(row, x, 0)
        length = length + str(item % 2)
    length = int(length, 2)
    for x in range(length):
        item = image.item(row, x+8, 0)
        rv = rv + str(item % 2)
    return int(rv, 2)


def convertToArray(image):
    rv = []
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            rv.append(image.item(x, y, 0))
    return rv


def convertToImage(array, size):
    bi = np.zeros((size, size, 3), np.uint8)
    i = 0
    for x in range(bi.shape[0]):
        for y in range(bi.shape[1]):
            bi.itemset((x, y, 0), array[i])
            bi.itemset((x, y, 1), array[i])
            bi.itemset((x, y, 2), array[i])
            i = i+1
    return bi


img = cv2.imread('/Users/tech4GT/Desktop/Images/IMG_0100.jpg')
inp = cv2.imread('/Users/tech4GT/Desktop/Images/crop.png')

arr = convertToArray(inp)


cv2.imshow('img', img)
cv2.imshow('inp', inp)
cv2.waitKey(0)
cv2.destroyAllWindows()

encode(img, len(arr), 0)

for i in range(len(arr)):
    val = arr[i]
    encode(img, val, i+1)

l = extract(img, 0)
op = []

for i in range(1, l+1):
    op.append(extract(img, i))

op = convertToImage(op, 35)

cv2.imshow('img', img)
cv2.imshow('op', op)
cv2.waitKey(0)
cv2.destroyAllWindows()
