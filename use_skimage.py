# !/usr/bin/env python
# confing:utf-8 
__author__ = "liyanhe"

import time
time_start = time.time()        #开始计时
import skimage
from skimage import filters,data,color
import numpy as np
from PIL import Image

pic_address = './picture/lena512color.jpg'

#打开图片
im = Image.open(pic_address)

#将图像转为灰度图像
im_change = im.convert('L')

img_array = np.array(im_change)


thresh = filters.threshold_otsu(img_array,nbins=256)   #返回一个阈值
print('阈值',thresh)

time_end = time.time()
print('usetime',time_end-time_start)