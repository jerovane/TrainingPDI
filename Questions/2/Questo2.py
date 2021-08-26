import cv2

# Read a rgb image
image = cv2.imread('image.jpg')

# Transform to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show the grayscale image
cv2.imshow('grayscale image', grayscale_image)
cv2.waitKey(0)

# Save the result
cv2.imwrite('grayscale_image.jpg', grayscale_image)
