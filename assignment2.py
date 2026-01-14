import cv2
# INPUTING FILE PATH
file_path=input("please enter the file path: ")
# READING FILE PATH
image=cv2.imread(file_path)
print("make rectangle: type1 \n draw line: type 2 \n add text : enter 3 ")
        
# INPUT FROM USERS             
user_choice=input("Please elect the options for you desired application")
# IF USER CHOICE IS 1 MAKE A RECTANGLE ACCORDING TO USERS GIVEN DIMENSIONS 
if user_choice=="1":
    # WE MAKE A TUPLE FOR STORING THE CORRDINATES AND MAPPED IT IN THE FORM OF INTEGER AND ECPECTING INPUT FROM USERS 
     p1 = tuple(map(int, input("Enter starting coordinate (x,y): ").split(",")))
     p2 = tuple(map(int, input("Enter ending coordinate (x,y): ").split(",")))
    #  MAKING A RECTANGLE OF P1 AND P2 , OF GREEN COLOR AND THICKNESS 2
     cv2.rectangle(image,p1,p2,(0,255,0),2)
     cv2.imshow("rectangle", image)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
# IF USER CHOICE IS 2 DRAW A LINE ACCORDING TO USERS GIVEN DIMENSIONS 
elif user_choice=="2":
    # WE MAKE A TUPLE FOR STORING THE CORRDINATES AND MAPPED IT IN THE FORM OF INTEGER AND ECPECTING INPUT FROM USERS 
      p1 = tuple(map(int, input("Enter starting coordinate (x,y): ").split(",")))
      p2 = tuple(map(int, input("Enter ending coordinate (x,y): ").split(",")))
    #  MAKING A LINE OF P1 AND P2 , OF GREEN COLOR AND THICKNESS 2
      cv2.line(image,p1,p2,(0,255,0),2)
      cv2.imshow("line", image)
      cv2.waitKey(0)
# IF USER CHOICE IS 3 ADD TEXT ACCORDING TO USERS GIVEN DIMENSIONS 
elif user_choice=="3":
      text=input("enter text to be displayed : ")
    # WE MAKE A TUPLE FOR STORING THE CORRDINATES AND MAPPED IT IN THE FORM OF INTEGER AND ECPECTING INPUT FROM USERS 
      position = tuple(map(int, input("Enter position (x,y): ").split(",")))
    #   ADDING TEXT IN THE IMAGE OF GIVEN USER TEXT , SETTING POSITION AND ADDING FONT , FONTTEXT-SIZE OF 1 , RED COLOR TEXT AND THICKNESS OF 2 
      cv2.putText(image, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
      cv2.imshow("text", image)
      cv2.waitKey(0)          
else:
      print("please select sutable option ")