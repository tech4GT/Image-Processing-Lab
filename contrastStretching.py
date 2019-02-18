import cv2
import numpy as np

# Calculate the max and min Intensity in the image
min = 255
max = 0
img = cv2.imread('./Images/contrast.jpg')
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        val = img.item(x, y, 1)
        if val > max:
            max = val
        elif val < min:
            min = val

print(min)
print(max)


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Final max and min contrast values
a = 0
b = 255

# Precompute the constant multiplier
c = (b-1)/(max-min)

for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        val = img.item(x, y, 0)
        val = ((val-min)*c) + a
        img.itemset((x, y, 0), val)
        img.itemset((x, y, 1), val)
        img.itemset((x, y, 2), val)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
