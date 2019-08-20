# !/usr/bin/env python
# confing:utf-8 
__author__ = "liyanhe"


import numpy as np


# 对个体x进行交叉
def cross(x):
    #生成掩码
    list1 = [1,2,4,6,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
    return np.bitwise_and(x, list1[np.random.randint(0,len(list1))])

def Crossover(pop,pc):

    coss_determination = np.random.randint(0,len(pop),size=[int(len(pop)*0.1),1])
    for i in coss_determination:
        pop[i] = cross(pop[i])
    return pop


