import cv2
import os

name = input('Enter student name : ')

path = f'dataset/{name}'
os.makedirs(path, exist_ok=True)

cam = cv2.VideoCapture(0)
count = 0

while True:
    ret ,frame = cam.read()
    cv2.imshow('Capture Images',frame)

    key = cv2.waitKey(1)

    if key == ord('s'):  # press S to save
        cv2.inwrite(f'{path}/(count).jpg',frame)
        count += 1
        print('Saved image',count)

    elif key == 27 :  # ESC to exit 
        break

cam.release()
cv2.destroyAllWindows()

