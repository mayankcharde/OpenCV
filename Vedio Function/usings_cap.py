import cv2

cap = cv2.VideoCapture(0)

# HERE WE ARE READING THE CAPTURED VIDEO
while True:
    ret, frame = cap.read()
    #  AGAR RETURN NHI HO RAHA TO EXIST KR DO BREAK KRO
    if not ret:
        print("could not read frame")
        break
    # SHOWING THE WEBCAM
    cv2.imshow("webcam feed", frame)
    # AGAR 'Q' PRESS KIYA TO VIDEO WILL CLOSE DUE TO ASCII VALUE OF Q 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quitting")
        break
    
cap.release()
cv2.destroyAllWindows()    
    