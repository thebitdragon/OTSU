# !/usr/bin/env python
# confing:utf-8 
__author__ = "liyanhe"

from PIL import Image
def target(img,M):
    """

    :param img:要传入的图像,图像为灰度图像
    :param M: 分割图像的阈值，灰度图像的话是0~255像素值中的一个值
    :return: otsu的最大类间方差
    """
    img_size = img.size
    m = img_size[0]
    n = img_size[1]
    img_array = img.load()
    m1 = 0
    m2 =0
    pix1 = 0
    pix2 = 0
    for i in range(0,m):
        for j in range(0,n):
            if img_array[i,j] <= M:
                m1 = m1 + 1
                pix1 = pix1 + img_array[i,j]
            else:
                m2 = m2 + 1
                pix2 = pix2 + img_array[i,j]
    w1 = m1 / (m*n)
    w2 = m2 / (m*n)
    if m1==0:
        u1 = 0
    else:
        u1 = pix1 / m1
    if m2==0:
        u2 = 0
    else:
        u2 = pix2 / m2

    #f = w1*(u1-(m1+m2)/(m*n))**2 + w2*(u2-(m1+m2)/(m*n))**2
    f = w1 * w2 * (u1 - u2) ** 2
    return f