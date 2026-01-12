import cv2

image = cv2.imread("Filtering and Blurrring/free-nature-images.jpg")
# HERE 15 MEANS BLURNESS LEVEL
blurred  =  cv2.medianBlur(image, 15)

cv2.imshow("original", image)
cv2.imshow("clean image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()