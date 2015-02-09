# -*- coding: utf-8 -*-
import cv2
import numpy

def salt(img, n):
    for k in range(n):
        i = int(numpy.random.random() * img.shape[1])
        j = int(numpy.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j,i] = 255
        elif img.ndim == 3:
            img[j,i,0]= 255
            img[j,i,1]= 255
            img[j,i,2]= 255
    return img

"""
过滤是信号和图像处理中基本的任务。其目的是根据应用环境的不同，选择性的提取图像中某些认为是重要的信息。
过滤可以移除图像中的噪音、提取感兴趣的可视特征、允许图像重采样，等等。
其源自于一般的信号和系统理论，这里将不介绍该理论的细节。但这里会介绍关于过滤的基本概念，
以及如何在图像处理程序中使用滤波器。首先，简要介绍下频率域分析的概念。

当我们观察一张图片时，我们观察的是图像中有多少灰度级（或颜色）及其分布。根据灰度分布的不同来区分不同的图像。
但还有其他方面可以对图像进行分析。我们可以观察图像中灰度的变化。某些图像中包含大量的强度不变的区域（如蓝天），
而在其他图像中的灰度变化可能会非常快（如包含许多小物体的拥挤的图像）。
因此，观察图像中这些变化的频率就构成了另一条分类图像的方法。这个观点称为频域。
而通过观察图像灰度分布来分类图像称为空间域。

频域分析将图像分成从低频到高频的不同部分。低频对应图像强度变化小的区域，而高频是图像强度变化非常大的区域。
目前已存在若干转换方法，如傅立叶变换或余弦变换，可以用来清晰的显示图像的频率内容。
注意，由于图像是一个二维实体，所以其由水平频率（水平方向的变化）和竖直频率（竖直方向的变化）共同组成。

在频率分析领域的框架中，滤波器是一个用来增强图像中某个波段或频率并阻塞（或降低）其他频率波段的操作。
低通滤波器是消除图像中高频部分，但保留低频部分。高通滤波器消除低频部分

这里介绍在OpenCV-Python中实现的初级的滤波操作，06中介绍更加复杂的滤波原理及其实现。
"""
# 用低通滤波来平滑图像
# 低通滤波器的目标是降低图像的变化率。如将每个像素替换为该像素周围像素的均值。
# 这样就可以平滑并替代那些强度变化明显的区域。在OpenCV中，可以通过blur函数做到这一点
# dst = cv2.blur(image,(5,5)); 
# 其中dst是blur处理后返回的图像，参数一是输入的待处理图像，参数2是低通滤波器的大小。
# 其后含有几个可选参数，用来设置滤波器的细节，具体可查阅参考资料2。不过这里，这样就够了。
img = cv2.imread("pics/face.png", 0)
result = cv2.blur(img, (5,5))

# 这种滤波器又称为boxfilter（注，这与化学上的箱式过滤器是两码事，所以这里就不翻译了）。
# 所以也可通过OpenCV的cv2.bofxfilter(...)函数来完成相同的工作。如下：
# result1 = cv2.boxFilter(img, -1, (5, 5))
# 这行代码与上面使用blur函数的效果完全相同。其中第二个参数的-1表示输出图像使用的深度与输入图像相同。
# 后面还有几个可选参数，具体可查阅OpenCV文档。
result1 = cv2.boxFilter(img, -1, (5, 5))

# 高斯模糊
# 在某些情况下，需要对一个像素的周围的像素给予更多的重视。因此，可通过分配权重来重新计算这些周围点的值。
# 这可通过高斯函数（钟形函数，即喇叭形数）的权重方案来解决。
# cv::GaussianBlur函数可作为滤波器用下面的方法调用：
# gaussianResult = cv2.GaussianBlur(img,(5,5),1.5)
# 低通滤波与高斯滤波的不同之处在于：低通滤波中，滤波器中每个像素的权重是相同的，即滤波器是线性的。
# 而高斯滤波器中像素的权重与其距中心像素的距离成比例。关于高斯模糊的详细内容，抽空将写一篇独立的文章介绍。
gaussianResult = cv2.GaussianBlur(img,(5,5),1.5)

# 使用中值滤波消除噪点
# 前面介绍的是线性过滤器，这里介绍非线性过滤器——中值滤波器。中值滤波器对消除椒盐现象特别有用。
# 调用中值滤波器的方法与调用其他滤波器的方法类似，如下：
# result = cv2.medianBlur(image,5)
# 函数返回处理结果，第一个参数是待处理图像，第二个参数是孔径的尺寸，一个大于1的奇数。
# 比如这里是5，中值滤波器就会使用5×5的范围来计算。即对像素的中心值及其5×5邻域组成了一个数值集，
# 对其进行处理计算，当前像素被其中值替换掉。
# 如果在某个像素周围有白色或黑色的像素，这些白色或黑色的像素不会选择作为中值（最大或最小值不用），
# 而是被替换为邻域值。

result2 = salt(img, 500)
median = cv2.medianBlur(result, 5)

cv2.imshow("Origin", img)
cv2.imshow("Blur", result)
cv2.imshow("Blur1", result1)
cv2.imshow("Gaussian", gaussianResult)
cv2.imshow("Salt", result2)
cv2.imshow("Median", median)


cv2.waitKey(0)
cv2.destroyAllWindows()