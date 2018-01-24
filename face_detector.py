import cv2
import dlib
import numpy as np


# 根据人脸框bbox，从一张完整图片裁剪出人脸
bgrImg = cv2.imread('test2.jpg')

# 图片格式转换BGR-RGB
rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

detector = dlib.get_frontal_face_detector()
faces = detector(rgbImg, 1)
print("faces number={}".format(len(faces)))

if len(faces) > 0:
    for face in faces:
        x1, x2, y1, y2 = face.left(), face.right(), face.top(), face.bottom()
        cv2.rectangle(bgrImg, (x1, y1), (x2, y2), (0, 0, 255), 1)
cv2.imshow("Image", bgrImg)
cv2.waitKey(0)
