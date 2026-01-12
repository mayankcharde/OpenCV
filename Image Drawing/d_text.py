import cv2

image = cv2.imread("Image Handelling Basic/python_image.png")

if image is None:
    print("oops!! your image is not working")
else:
    print("image load successfully")
    # HERE WE ARE GIVING TEXT FIRST, (50,300) IS THE WIDTH AND HEIGHT WHERE THE TEXT ALIGN
    # THEN FONT , 1.2 IS THICKNES OF FONT 
    # THEN COLOR BLUE AND THICKNESS 2 
    cv2.putText(image,"hello python", (50,300), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,0,0),2)
    
    cv2.imshow("adding text over image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    