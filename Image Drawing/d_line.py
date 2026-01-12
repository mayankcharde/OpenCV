import cv2

image = cv2.imread("Image Handelling Basic/python_image.png")


if image is None:
    print("oops! your image is not working")
else:
    print("image load successfully")
    # THIS IS BASICALLY WIDTH AND HEIGHT OF POINT 1 AND 2
    pt1 = (50,100)
    pt2 = (300,100)
    color = (255,0,0)
    thickness = 4
    
    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow("line drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    