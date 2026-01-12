# Loads the OpenCV library so we can work with images.
import cv2

image = cv2.imread("Image Resizing and Shaping/python_image.png")

if image is None:
    print("could not load image")
    
else:
    # image.shape gives (height, width, channels).

# We only take height and width.

# Example: h = 600, w = 800.
# HERW WE USE :2 BECAUSE FROM FIRST WE ARE ONLY TAKING HEIGHT AND WIDTH ONLY
    (h,w) = image.shape[:2]
    
    # // means integer division.

# This center is used as the rotation pivot.
    center = (w//2,h//2)
    # HERE CENTER IS POINT AROUND WHICH IMAGE ROTATE
    # 90 MEANS THE ANGLE
    #  1.0 MEANS SCALE FACTOR
    M= cv2.getRotationMatrix2D(center, 90, 1.0)
    # HERE WE ARE APPLYING THE ROTATION TO THE IMAGE
    # AND APPLYING TRANSFORMATION MATRIX 
    rotated = cv2.warpAffine(image, M,(w,h))
    
    cv2.imshow("original", image)
    cv2.imshow("rotated 90", rotated) 
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()   