import numpy as np
import cv2

black = np.zeros([150, 200, 1], 'uint8')
cv2.imshow("Black", black)
print(black[0, 0, :])

black1 = np.zeros([100, 150, 3], 'uint8')
cv2.imshow("Black1", black1)
print(black1[0, 0, :])

ones = np.ones([150, 200, 3], 'uint8')
cv2.imshow("Ones", ones)
print(ones[0, 0, :])

ones1 = np.ones([150, 200, 3], 'uint16')
cv2.imshow("Ones", ones1)
print(ones[0, 0, :])


white = np.ones([200, 200, 3], 'uint16')
white *= (2**16-1)
cv2.imshow("White", white)
print(white[0, 0, :])

blue = ones.copy()
blue[:, :] = (255, 0, 0)
cv2.imshow("Blue", blue)
print(blue[0, 0, :])

Red = ones.copy()
Red[:, :] = (0, 0, 255)
cv2.imshow("Red", Red)
print(Red[0, 0, :])

Green = np.ones([200, 200, 3 ],'uint8')
Green[:,:] = (0, 255, 0)
cv2.imshow("Green", Green)
print(Green[0, 0, :])

cv2.waitKey(0)
cv2.destroyAllWindows()