import cv2

#Read a rgb image
image = cv2.imread('image.jpg')

#Show a rgb image
cv2.imshow('image', image)
cv2.waitKey(0)

#Saved the loaded image
cv2.imwrite('saved_image.jpg', image)