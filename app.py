import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    #Capture video frame by frame
    ret, frame = cap.read()
    width = int(cap.get(3)) #width needs to be int instead of float for slice later
    height = int(cap.get(4)) #height

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (100, 100), (200,200), (128, 128, 128), 5)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Test text!', (50, height - 10), font, 4, (0, 0, 0), 5, cv2.LINE_AA) #text, center position , font, font scale, color, line thickness, line type

    #Display each frame
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break


# After the loop release the cap object (relase our webcam so it can be used by other programs)
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()