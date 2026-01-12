import cv2

image = cv2.imread("Image Handelling Basic/python_image.png")


if image is None:
    print("error: image not found")
else:
    print("image load successfully!!")    