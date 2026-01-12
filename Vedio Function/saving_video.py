import cv2

camera = cv2.VideoCapture(0)

# 🔹 Gets webcam frame size.
# CAP_PROP_FRAME_WIDTH → width of camera frames
# CAP_PROP_FRAME_HEIGHT → height of camera frames
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 'XVID' is a common AVI codec.
# Converts characters into a fourcc code.FOR COMPORESSION
codec = cv2.VideoWriter_fourcc(*'XVID')

# HERE 20 IS FPS
recorder = cv2.VideoWriter("my_vedio.avi", codec, 20, (frame_width, frame_height))

while True:
    success, image = camera.read()
    
    if not success:
        break
    
    # Writes the current frame into the video file.
    recorder.write(image)
    # Displays the live video on screen.
    cv2.imshow("recording live", image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

camera.release()
recorder.release()
cv2.destroyAllWindows()