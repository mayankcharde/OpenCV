import cv2
img = cv2.imread("Edge Detection/man.png", cv2.IMREAD_GRAYSCALE)

# gray	Input grayscale image
# 200	Threshold value
# 255	Maximum value
# THRESH_BINARY	Binary threshold type
# ret means return
ret, thresh_img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("original image", img)
cv2.imshow("threshold image", thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()