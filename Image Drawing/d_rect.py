import cv2

image = cv2.imread("Image Handelling Basic/python_image.png")


if image is None:
    print("oops!! wrong image")
else:
    print("image load successfully")
    pt1=(50,50)    
    pt2 = (250,200)
    
    color = (0,0,255)
    thickness = 3
    
    cv2.rectangle(image,pt1,pt2,color,thickness)
    
    cv2.imshow("image load successfully", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()