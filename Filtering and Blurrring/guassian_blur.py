import cv2

image = cv2.imread("Filtering and Blurrring/free-nature-images.jpg")
#  KERNEL (7,7) IS PIXEL WINDOW THAT MOVES OVER THE IMAGE
# MORE THE VALUE MORE THE IMAGE WILL BE BLURRED
# LARGER KERNEL MORE BLUR
# MUST BE ODD NUMBERS
# 3 IS GAUSIAN SMOOTHING THAT CONTROLS SMOOTHING AND BLURRINESS OF THE IMAGE
blurred = cv2.GaussianBlur(image, (3,3) , 1)

cv2.imshow("original image", image)
cv2.imshow("blurred image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()