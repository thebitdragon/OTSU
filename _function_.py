# !/usr/bin/env python
# confing:utf-8 
__author__ = "liyanhe"

from PIL import Image
from target import target

pic_address = '/home/liyanhe/图片/taishan.jpg'

# 打开图片
im = Image.open(pic_address)

# 将图像转为灰度图像
im_change = im.convert('L')

def obj_function(x):
    """

    :param x: 传入otsu的阈值
    :return: 相应阈值的最大类间方差
    """
    y = target(im_change,x)

    return y


def fit_function(x):
    """

    :param x: 传入otsu的阈值
    :return: 相应阈值的最大类间方差
    """
    y = target(im_change,x)

    return y

def ufit_function(x):
    """

    :param x: 传入otsu的阈值
    :return: 相应阈值的最大类间方差
    """
    y = target(im_change,x)

    return -1*y