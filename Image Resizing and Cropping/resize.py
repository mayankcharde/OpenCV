import cv2

image = cv2.imread("Image Resizing and Shaping/python_image.png")


if image is None:
    print("image not found")
else:
    print("image loaded")
    # THIS 300 AND 300 IS WIDTH AND HEIGHT 
    resized = cv2.resize(image,(300,300))
    
    cv2.imshow("original image", image)
    cv2.imshow("resized image", resized)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()    