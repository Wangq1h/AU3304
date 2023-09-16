import cv2

# 读取图像并转换为灰度图像
image = cv2.imread('pill.png')
image = cv2.GaussianBlur(image, (3, 3), 0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 二值化处理
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite('pill_binary.png', binary)

# 查找连通域
"""
调整下行代码中cv2.connectedComponentsWithStats()函数中的参数connectivity -> 指示连通域的类型
改成4连通域,观察检测结果会有什么变化,放大观察pill_binary.png分析产生变化的原因
"""
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)

# 打印连通域的个数
print("Number of connected components:", num_labels - 1)  # 减去背景连通域

# 打印每个连通域的面积
for i in range(1, num_labels):
    area = stats[i, cv2.CC_STAT_AREA]
    print("Area of connected component", i, ":", area)

# 可视化连通域
output = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
for i in range(1, num_labels):
    color = (0, 0, 255)  # 红色
    cv2.rectangle(output, (stats[i, cv2.CC_STAT_LEFT], stats[i, cv2.CC_STAT_TOP]),
                  (stats[i, cv2.CC_STAT_LEFT] + stats[i, cv2.CC_STAT_WIDTH],
                   stats[i, cv2.CC_STAT_TOP] + stats[i, cv2.CC_STAT_HEIGHT]), color, 2)
    cv2.putText(output, str(i), (int(centroids[i, 0]), int(centroids[i, 1])),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# 显示图像和连通域
cv2.imshow('Image', image)
cv2.imshow('Connected Components', output)
cv2.waitKey(0)
cv2.destroyAllWindows()