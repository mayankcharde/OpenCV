import cv2
import numpy as np

# Creates two 300×300 black images
# uint8 means pixel values range from 0 to 255
img1=np.zeros((300,300), dtype="uint8")
img2=np.zeros((300,300), dtype="uint8")

# HERE 255 IS WHITE COLOR AND -1 IS FILLED CIRCLE
cv2.circle(img1, (150,150), 100, 255 ,-1)
#  HERE WE HAVE TOP-LEFT AND BOTTOM-RIGHT CORNER 
#  255 WHITE COLOR AND -1 IS FILLED RECTANGLE
cv2.rectangle(img2,(100,100), (250,250), 255, -1)

# Keeps only the region where both images have white pixels.
bitwise_and = cv2.bitwise_and(img1, img2)
# Keeps all white areas from either image.
bitwise_or = cv2.bitwise_or(img1, img2)
# Inverts colors of img1.
bitwise_not = cv2.bitwise_not(img1)


cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()