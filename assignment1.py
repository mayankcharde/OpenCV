import cv2


# HERE WE ARE ACCEPTING THE PATH OF THE IMAGE
path = input("Enter path of the image: ")
# READING IMAGE PATH
img = cv2.imread(path)
if img is None:
    print("Image not loaded")
else:
    print("Image loaded sucessfully")
    # CONVERTING IMAGE TO GRAY SCALE FOR FAST PROCCESSING
cvt_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# MAKING INPUT
a = input("What you want(show/save the image): ").strip().lower()
if a == "show":
    cv2.imshow("Data science image",cvt_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif a == "save":
    b = input("Enter the image output name: ")
    sucess = cv2.imwrite(f"{b}.jpg" ,  cvt_img)
    if sucess:
       print("Image saved")
    else:
       print("Image not save")