import numpy as np

oneX = 5
oneY = 7
twoX = 3
twoY = 2

print("Euclid: ")
print(np.sqrt(np.power((oneX-twoX), 2) + np.power(oneY-twoY, 2)))
print("City block: ")
print(np.absolute(oneX-twoX) + np.absolute(oneY-twoY))
print("Chessboard: ")
print(max(np.absolute(oneX-oneY), np.absolute(oneY-twoY)))
