import cv2
import numpy as np
import math

img = cv2.imread('/Users/tech4GT/Desktop/Images/photo.jpeg')

# get the factor by which to enlarge
c = int(input("\nEnter the factor by which to zoom\n"))

# Get which interpolation to apply
ip = int(input("\nChoose the interpolation\n1: Nearest Neighbor\n2: Bilinear\n"))

# create the output image
op = np.zeros((img.shape[0]*c, img.shape[1]*c, 3), np.uint8)

# Invalid Optionn
if(ip != 1 and ip != 2):
    print("Invalid Option\n")
    exit(1)

# Nearest Neighbor interpolation
elif ip == 1:

    # Set the actual values in the new image at the right positions
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            for channel in range(3):
                op.itemset((c*x, c*y, channel), img.item(x, y, channel))

    # Go to every pixel containing actual value and set it's neighbors
    for x in range(0, op.shape[0], c):
        for y in range(0, op.shape[1], c):
            for i in range(math.ceil(x-c/2), math.ceil(x+c/2)):
                for j in range(math.ceil(y-c/2), math.ceil(y+c/2)):
                    if i >= 0 and i < op.shape[0] and j >= 0 and j < op.shape[1]:
                        for channel in range(3):
                            op.itemset((i, j, channel), op.item(x, y, channel))

else:

    # Set the pixels with actual pixel values
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            for channel in range(3):
                op.itemset((c*x, c*y, channel), img.item(x, y, channel))

    # Horizontal Interpolation
    for x in range(0, op.shape[0], c):
        for y in range(0, op.shape[1], c):
            for dist in range(1, c):
                for channel in range(3):
                    val = 0
                    if y+c < op.shape[1]:
                        val = round((op.item(x, y, channel)*dist +
                                     op.item(x, y+c, channel)*(c-dist))/c)
                    else:
                        val = op.item(x, y, channel)
                    op.itemset((x, y+dist, channel), val)

    # Vertical Interpolation
    for x in range(0, op.shape[0], c):
        for y in range(0, op.shape[1]):
            for dist in range(1, c):
                for channel in range(3):
                    val = 0
                    if x+c < op.shape[0]:
                        val = round((op.item(x, y, channel)*dist +
                                     op.item(x+c, y, channel)*(c-dist))/c)
                    else:
                        val = op.item(x, y, channel)
                    op.itemset((x+dist, y, channel), val)


# Display the image
cv2.imshow('input', img)
cv2.imshow('output', op)
cv2.waitKey(0)
cv2.destroyAllWindows
