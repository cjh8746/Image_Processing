import numpy as np
import cv2

def onChange(value):
    global image, title                         # 전역 변수 참조

    add_value = value - int(image[0][0])        # 트랙바 값과 영상 화소값 차분
    print("추가 화소값:", add_value)
    image = image + add_value                   # 행렬과 스칼라 덧셈 수행
    cv2.imshow(title,image)

def onMouse(event, x,y,flags,param):
    global image, bar_name

    if event == cv2.EVENT_RBUTTONDOWN:
        if(image[0][0] < 246) : image = image + 10
        cv2.setTrackbarPos(bar_name, title, image[0][0]) #트랙바 위치 변경
        cv2.imshow(title,image)

    elif event == cv2.EVENT_LBUTTONDOWN:
        if(image[0][0] >= 10):
            image = image - 10
            cv2.setTrackbarPos(bar_name,title,image[0][0])
            cv2.imshow(title,image)


image = np.zeros((300,500),np.uint8)
title = "Tracker & Mouse Event"
bar_name = "Brightness"
cv2.imshow(title,image)

cv2.createTrackbar(bar_name, title, image[0][0],255, onChange)
cv2.setMouseCallback(title,onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

