import numpy as np
import cv2
import dlib


def add_hat(img, hat_img):
    # 分离rgba通道，合成rgb三通道帽子图，a通道后面做mask用
    r, g, b, a = cv2.split(hat_img)
    rgb_hat = cv2.merge((r, g, b))
    cv2.imwrite("hat_alpha.jpg", a)

    # dlib人脸关键点检测器
    predictor_path = "shape_predictor_5_face_landmarks.dat"
    predictor = dlib.shape_predictor(predictor_path)

    # dlib正脸检测器
    detector = dlib.get_frontal_face_detector()


    return 0


def main():
    # 读取帽子图，第二个参数-1表示读取为rgba通道，否则为rgb通道
    hat_img = cv2.imread("hat2.png", -1)

    # 读取头像图
    img = cv2.imread("test.jpg", 0)

    # 在头像上加圣诞帽子
    output = add_hat(img, hat_img)

    # 显示加帽子后的图片
    cv2.imshow("output", output)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()

