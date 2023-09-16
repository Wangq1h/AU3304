import cv2


#---------------------图像的读取、显示和写入--------------------#
# 读取图像
image = cv2.imread('lena.jpg')

# 显示图像
cv2.imshow('lena', image)
#等待用户按下键盘上的任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 显示图像
cv2.imshow('lena_gray', gray)
#等待用户按下键盘上的任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
# 写入图像
cv2.imwrite('lena_gray.jpg', gray)

# 转换为二值图像
"""
调整下行代码中cv2.threshold()函数中第二位置上参数的数值(在[0,255]之间变化),观察结果会有什么变化
"""
ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# 显示图像
cv2.imshow('lena_bin', binary)
#等待用户按下键盘上的任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
# 写入图像
cv2.imwrite('lena_bin.jpg', binary)


#-------------------------RGB空间和HSI空间------------------------#
src = cv2.imread("opencv.png")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# 显示红色通道
mv = cv2.split(src)
# 其他两个通道置零
mv[0][:, :] = 0
mv[1][:, :] = 0
dst1 = cv2.merge(mv)
cv2.imshow("Red channel", dst1)

# 显示绿色通道
mv = cv2.split(src)
# 其他两个通道置零
mv[0][:, :] = 0
mv[2][:, :] = 0
dst2 = cv2.merge(mv)
cv2.imshow("Green channel", dst2)

# 显示蓝色通道
mv = cv2.split(src)
# 其他两个通道置零
mv[1][:, :] = 0
mv[2][:, :] = 0
dst3 = cv2.merge(mv)
cv2.imshow("Blue channel", dst3)

#等待用户按下键盘上的任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

# 将RGB图像转换为HSV图像
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 分割HSV图像的单通道
h, s, v = cv2.split(hsv_image)

# 显示RGB图像和单通道图像
cv2.imshow('RGB Image', image)
cv2.imshow('H Channel', h)
cv2.imshow('S Channel', s)
cv2.imshow('V Channel', v)

#等待用户按下键盘上的任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()