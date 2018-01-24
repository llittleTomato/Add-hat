import numpy as np
import cv2
import dlib


def add_hat():

    return 0


def main():
    # 读取帽子图，第二个参数-1表示读取为rgba通道，否则为rgb通道
    hat_img = cv2.imread("hat2.png", -1)

    # 读取头像图
    img = cv2.imread("test.jpg", 0)

    # 分离rgba通道，合成rgb三通道帽子图，a通道后面做mask用
    r, g, b, a = cv2.split(hat_img)
    rgb_hat = cv2.merge((r, g, b))
    cv2.imwrite("hat_alpha.jpg", a)

    #在头像上加圣诞帽子
    # output = add_hat(img, cv2.imread("hat2.png", 0)

    # 显示加帽子后的图片
    cv2.imshow("output", a)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()

