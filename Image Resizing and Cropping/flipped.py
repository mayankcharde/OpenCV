# import cv2

# image = cv2.imread("Image Handelling Basic/python_image.png")


# if image is not None:
#     print("could not load image")
# else:
#     flipped_horizontal = cv2.flip(image,1)    
#     flipped_vertical = cv2.flip(image,0)    
#     flipped_both = cv2.flip(image,-1)
    
#     cv2.imshow("origial", image)    
#     cv2.imshow("horizontal", flipped_horizontal)    
#     cv2.imshow("vertical", flipped_vertical)    
#     cv2.imshow("both", flipped_both)
    
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()    




import cv2

image = cv2.imread("Image Resizing and Shaping/python_image.png")

if image is None:
    print("Could not load image")
else:
    flipped_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("Original", image)
    cv2.imshow("Flipped Horizontal", flipped_horizontal)
    cv2.imshow("Flipped Vertical", flipped_vertical)
    cv2.imshow("Flipped Both", flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()