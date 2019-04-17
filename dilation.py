import numpy as np
import cv2


def dilate(img, se):
    imgOut = np.copy(img)

    def isValid(img, coord):
        x = coord[0]
        y = coord[1]
        if x >= 0 and x < img.shape[0] and y >= 0 and y < img.shape[1] and img.item(x, y, 0) > 50:
            return True
        else:
            return False
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            flag = False
            intensity = 255
            for coord in se:
                if isValid(img, (x+coord[0], y+coord[1])):
                    flag = True
                    # intensity = img.item(x+coord[0], y+coord[1], 0)
                    break
            if flag:
                imgOut.itemset((x, y, 0), intensity)
    return imgOut


if __name__ == "__main__":

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
    se = [(-1, -1), (1, -1), (-1, 1), (1, 1), (-1, 0), (0, -1),
          (0, 0), (0, 1), (1, 0), (-2, -2), (-2, -1), (-2, 0)]
    ip = np.copy(img)
    img = dilate(img, se)
    cv2.imshow('input', ip)
    cv2.imshow('output', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
