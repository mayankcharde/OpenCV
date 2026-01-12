import cv2

image = cv2.imread("Image Handelling Basic/python_image.png")

if image is not None:
    success = cv2.imwrite("output_python.png", image)
    if success:
        print("image saved successfully")
    else:
        print("error")    