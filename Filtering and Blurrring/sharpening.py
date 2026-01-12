import cv2

import numpy as np

image = cv2.imread("Filtering and Blurrring/free-nature-images.jpg")
# The center value 5 keeps the main pixel strong.

# The surrounding -1 values subtract neighboring pixel intensities.

# This increases edge contrast, making the image look sharper.
sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
# -1 IS OUTPUT IMAGE DEPTH
sharpened = cv2.filter2D(image, -1, sharpen_kernel)

cv2.imshow("original image", image)
cv2.imshow("sharpened image", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()