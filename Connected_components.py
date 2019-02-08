import cv2
import numpy as np

img = np.zeros((1000, 1000, 1), np.uint8)
op = np.zeros((1000, 1000, 1), np.uint8)

# Create the image for running the algorithm
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        if(x > 100 and x <= 200 and y <= 200 and y > 100):
            img.itemset((x, y, 0), 255)
        if(x > 400 and x <= 800 and y > 100 and y <= 200):
            img.itemset((x, y, 0), 255)
        if(x > 600 and x <= 800 and y > 200 and y <= 600):
            img.itemset((x, y, 0), 255)
        if(x > 400 and x <= 800 and y > 600 and y <= 700):
            img.itemset((x, y, 0), 255)
        if(x > 400 and x <= 600 and y > 300 and y <= 500):
            img.itemset((x, y, 0), 255)

# Run the component labelling 2 pass algorithm

eq = {}
classes = {}
classCount = 0

""" first pass """
for x in range(img.shape[0]):
    for y in range(img.shape[1]):

        if(img.item(x, y, 0) == 0):
            continue

        if(x > 0 and img.item(x-1, y, 0) != 0 and y > 0 and img.item(x, y-1, 0) != 0):
            classes[str(x) + "-" + str(y)] = min(classes[str(x-1) + "-" + str(y)],
                                                 classes[str(x) + "-" + str(y-1)])
            eq[classes[str(x-1) + "-" + str(y)]
               ] = classes[str(x) + "-" + str(y)]
            eq[classes[str(x) + "-" + str(y-1)]
               ] = classes[str(x) + "-" + str(y)]
        elif(x > 0 and img.item(x-1, y, 0) != 0):
            classes[str(x) + "-" + str(y)] = classes[str(x-1) + "-" + str(y)]
        elif(y > 0 and img.item(x, y-1, 0) != 0):
            classes[str(x) + "-" + str(y)] = classes[str(x) + "-" + str(y-1)]
        else:
            classes[str(x) + "-" + str(y)] = classCount
            eq[classCount] = classCount
            classCount = classCount+1


""" second pass """
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        if(img.item(x, y, 0) == 0):
            continue
        classes[str(x) + "-" + str(y)] = eq[classes[str(x) + "-" + str(y)]]

# print(eq)

colors = {
    0: 40,
    1: 100,
    2: 150,
    3: 200,
    4: 255
}

for x in range(img.shape[0]):
    for y in range(img.shape[1]):

        if(img.item(x, y, 0) != 0):
            op.itemset((x, y, 0), colors[classes[str(x) + "-" + str(y)]])

cv2.imshow("input", img)
cv2.imshow("output", op)
cv2.waitKey(0)
cv2.destroyAllWindows()
