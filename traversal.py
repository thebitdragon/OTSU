# !/usr/bin/env python
# confing:utf-8 
__author__ = "liyanhe"

import time
time_start = time.time()        #开始计时
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from target import target

"""
读取图像获得相关参数
"""
pic_address = './picture/lena512color.jpg'

#打开图片
im = Image.open(pic_address)

#将图像转为灰度图像
im_change = im.convert('L')

#读取图片尺寸大小
m = im_change.size[0]    #图片长
n = im_change.size[1]    #图片宽
#print ("长=",m,"\t宽=",n)
#读取像素值
im_array = im_change.load()


"""
遍历0~255的像素值
得到
"""
list0 = []
for i in range(0,255):
    list0.append(target(im_change,i))
max_fx = max(list0)                     #得到最大类间方差
M = list0.index((max_fx))               #得到阈值
print("最大类间方差=",max_fx,"\t阈值=",M)



# """
# 输出结果
# """
# #输出初始图像
# plt.figure('初始')
# plt.imshow(im)
#
# #输出otsu分割后的图像
# img = np.array(np.zeros([n,m],dtype=int))
# for i in range(0,n):
#     for j in range(0,m):
#         if im_array[j,i] <= M:
#             img[i,j] = 0
#         else:
#             img[i,j] = 255
# plt.figure('otsu')
# plt.imshow(img)


time_end = time.time()      #结束计时
print('usetime:',time_end - time_start)

plt.show()