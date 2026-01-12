import cv2

face_cascade = cv2.CascadeClassifier("Face and Object Detection/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("Face and Object Detection/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("Face and Object Detection/haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0,255,0), 2)

        """
        x,y - top=left corner

        (x+w, y+h)

        face = [
        (100,150,80,80) face1
        (250,120,90,90) face2
        ]
        x - how far from left
        y - how far from top
        w - width of face
        h - height of face
        """

        roi_gray = gray[y:y+h, x:x+w]
        #gray[150:150+80, 100:100+80]
        roi_color = frame[y:y+h, x:x+w]
        
        """
        x = 100
        y = 150
        w = 80
        h = 80

        (100,150)
        w = 80 > 180
        h = 80 > 230
        """
        
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes)>0:
            # HERE (X,Y-10) IS ADJUSTING WHERE THE TEXT IS VISIBLE FROM X AND Y AXIS
            cv2.putText(frame, "eyes detected", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255),2)
            
        
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        if len(smiles) > 0:
            # HERE (X,Y-10) IS ADJUSTING WHERE THE TEXT IS VISIBLE FROM X AND Y AXIS
            cv2.putText(frame, "Smiling", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
        
    cv2.imshow("Smart face detector", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()