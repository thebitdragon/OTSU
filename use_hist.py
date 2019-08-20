# !/usr/bin/env python
# confing:utf-8 
__author__ = "liyanhe"

import time
time_start = time.time()        #开始计时
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

pic_address = './picture/taishan.jpg'

#打开图片
im = Image.open(pic_address)

#将图像转为灰度图像
im_change = im.convert('L')

img_array = np.array(im_change)

im_array_1w = img_array.flatten()

hist , bin_edges = np.histogram(im_array_1w,bins=np.arange(65537))        #hist对应像素的点数，bin_edges表示0~65534的像素值

cumsum_hist = np.cumsum(hist)       #对应像素的点数的累加

bin_edges = bin_edges[:-1]      #像素点列表，0~65535

x_fx = hist*bin_edges       #像素值与对应该像素的点数相乘，当前像素总值

cumsum_x_fx = np.cumsum(x_fx)       #当前像素总值累加

u = cumsum_x_fx[-1]/cumsum_hist[-1]     #计算总像素点的平均值


"""
w0:前景像素点占比
w1:背景像素点占比
u1:前景像素点的像素平均值
u2:背景像素点的平均值
u:总像素点的像素平均值
"""
def the_bigest_var(T):
    w0 = cumsum_hist[T]/cumsum_hist[-1]
    w1 = 1 - w0

    if w0 == 0:
        u0 = 0
    else:
        u0 = cumsum_x_fx[T] / cumsum_hist[T]
    if w1 == 0:
        u1 = 0
    else:
        u1 = (u - w0*u0) / w1
    f = w0*w1*(u0-u1)**2
    return f

list1 = np.zeros(65536)
for i in bin_edges:
    list1[i] = the_bigest_var(i)

print('最大类间方差：',np.max(list1))
print('阈值：',np.argmax(list1))



time_end = time.time()
print('usetime',time_end - time_start)
