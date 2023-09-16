import cv2
import numpy as np

"""
查询各个变换函数中参数的含义,调整参数,观察不同参数下的结果
"""
#-----------------------------平移变换------------------------------#
# 读取图像
image = cv2.imread('lena.jpg')

# 定义平移矩阵
tx = 50  # 平移的像素数目
ty = 30
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# 应用平移变换
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# 显示原始图像和平移后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
#等待用户按下键盘上的任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
#-----------------------------平移变换------------------------------#



#-----------------------------旋转变换------------------------------#
# 读取图像
image = cv2.imread('lena.jpg')

# 定义旋转中心和角度
center = (image.shape[1] // 2, image.shape[0] // 2)  # 图像中心点坐标
angle = 45  # 旋转角度

# 获取旋转矩阵
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

# 应用旋转变换
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

# 显示原始图像和旋转后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
#等待用户按下键盘上的任意键后关闭窗口
cv2.destroyAllWindows()
#-----------------------------旋转变换------------------------------#



#-----------------------------缩放变换------------------------------#
# 读取图像
image = cv2.imread('lena.jpg')
# 定义缩放因子
scale_x = 0.5  # x轴缩放因子
scale_y = 0.5  # y轴缩放因子

# 缩放图像
scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y)

# 显示原始图像和缩放后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Scaled Image', scaled_image)
#等待用户按下键盘上的任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
#-----------------------------缩放变换------------------------------#



#-----------------------------翻转变换------------------------------#
import cv2

# 读取图像
image = cv2.imread('lena.jpg')

# 水平翻转
flipped_horizontal = cv2.flip(image, 1)

# 垂直翻转
flipped_vertical = cv2.flip(image, 0)

# 水平和垂直翻转
flipped_both = cv2.flip(image, -1)

# 显示原始图像和翻转后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Flipped Horizontal', flipped_horizontal)
cv2.imshow('Flipped Vertical', flipped_vertical)
cv2.imshow('Flipped Both', flipped_both)
#等待用户按下键盘上的任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
#-----------------------------翻转变换------------------------------#