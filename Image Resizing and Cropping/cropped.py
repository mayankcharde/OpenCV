import cv2
image = cv2.imread("Image Handelling Basic/python_image.png")

if image is not None:
    # THIS MEANS 100 TO 200 FROM TOP TO BOTTOM 
    #  AND 50 TO 150 FROM LEFT TO RIGHT
    cropped = image[100:200, 50:150]
    
    cv2.imshow("original", image)
    cv2.imshow("cropped", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()