import cv2

image = cv2.imread("Image Handelling Basic/python_image.png")

if image is not None:
    cv2.imshow("image showing", image) # open the window
    cv2.waitKey(0) # wait for a key
    cv2.destroyAllWindows() # close the window
else:
    print("could not load the image")    