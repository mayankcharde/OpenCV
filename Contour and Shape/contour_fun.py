import cv2

# Contours are the outlines or boundaries of objects in an image.
img = cv2.imread("Contour and Shape/circle.png")
# HERE WE ARE CONVERTING IMAGE TO GRAYSCALE
# BECAUSE CONTOURS ARE WORKS WELL IN GRAYSCALE IMAGES
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# HERE WE APPLY BINARY THRESHOLD 
# 200 IS THRESHOLD VALUE IF PIXEL GE THAN 200 WHITE AND 255 MAX VALUE 
# AND AT LAST IT IS BINARY THRESHOLD TYPE 
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# FIND CONTOURS 
# RETR_TREE IS RETRIVE FULL CONTOUR HIERATCHY
# AND COMPRESS CONTOUR POINTS TO SAVE TO MEMORY
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# -1 IS DRAW ALL CONTOURS , GREEN COLOR AND THICKNESS
cv2.drawContours(img,contours,-1,(0,255,0),3)

for contour in contours:
    # approxPolyDP:Removes unnecessary points and keeps only corner points.
    # Calculates perimeter of contour.

# 🔹 epsilon = 0.01 × perimeter

# Controls approximation accuracy.
# Smaller value → more precise shape.
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True), True)
    
    corners = len(approx)
    if corners == 3:
        shape_name = "Triangle"
        
    elif corners == 4:
        shape_name = "Rectangle"
    
    elif corners == 5:
        shape_name = "Pentagon"
    
    elif corners > 5:
        shape_name = "Circle"
    
    else:
        shape_name = "unknown"
        # HERE WE ARE DRAWING BOUNDRIES BASICALLY CONTOURS 
        # O MEANS IDX 
        # COLOR AND THICKNESS
    cv2.drawContours(img, [approx],0,(0,255,0) ,2)
    
    # BASICALLY RAVEL FUNCTION CONVERTS 3D ARRAY TO 1D ARRAY
    # IT IS X COORDINATES FROM IDX 0
    x= approx.ravel()[0]
    """
      [
    [[100,200]],
    [[150,250]],
    [[120,270]],
    ]
    [100,200,150,250,120,270]
    """ 
    # IT IS Y CORDINATE FROM IDX 1 
    # If we write text exactly on the contour line, it overlaps the shape.

# So subtracting 10:
# ✔ Moves text slightly above the shape
# ✔ Makes label clearly visible
    y=approx.ravel()[1] -10
    
# img	Image where text will be written
# shape_name	Text string ("Triangle", "Circle", etc.)
# (x,y)	Position where text starts
# FONT_HERSHEY_SIMPLEX	Font style
# 0.6	Font size (scale)
# (255,0,0)	Text color → Blue (BGR format)
# 2	Thickness of text
    cv2.putText(img, shape_name, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)
    
    cv2.imshow("contours", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()