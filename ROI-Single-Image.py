#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports
import cv2

# Read image
image = cv2.imread("Images/003.jpg")

# Convert to grayscale
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Crop the image using array slices - ROI
# First - height, Second - width
cropped = image[150:450, 500:800]

# Display ROI images
cv2.imshow("Cropped", cropped)

# Save images
cv2.imwrite('cropped.jpg',cropped)

# Waits to press any key
cv2.waitKey(0)

# Closes displayed windows
cv2.destroyAllWindows()