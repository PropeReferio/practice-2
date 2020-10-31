import numpy as np
import cv2

#Load a color image in grayscale
clau = cv2.imread('firstnight.jpg', -1)
cv2.imshow('image', clau)
cv2.waitKey(3000)
cv2.destroyAllWindows() # TODO jump outta planes

True