import cv2

image = cv2.imread("Image Handelling Basic/python_image.png")

if image is None:
    print("oops! you image is not working")
else:
    print("image loaded successfully!!")
    # HERE WE ADDING THE IMAGE 
    # (210,150) IS CENTER COORDINATES OF CIRCLE
    # 50 IS RADIUS OF CIRCLE
    # AND BLUE COLOR AND 5 IS THICKNESS
    cv2.circle(image, (210,150),50,(255,0,0),5)
    
    cv2.imshow("drawing circle", image)
    cv2.waitKey()
    cv2.destroyAllWindows()    