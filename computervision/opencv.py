import cv2

img = cv2.imread('dog.png')
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

cv2.imshow('dog image',gray)

cv2.waitKey(5000)
cv2.destroyAllWindows()