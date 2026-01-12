import cv2

img = cv2.imread("Edge Detection/flower.png", cv2.IMREAD_GRAYSCALE)
# It finds and highlights edges (boundaries) in the image.
# HERE 50 IS LOWER AND 150 IS HIGHER THRESHOLD VALUE
edges = cv2.Canny(img, 50,150)

cv2.imshow("original image", img)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()