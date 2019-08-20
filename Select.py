# !/usr/bin/env python
# confing:utf-8 
__author__ = "liyanhe"


import numpy as np
from used_function import fit_function
from used_function import ufit_function
def Select(pop,ps):
    popsize = len(pop)      #种群规模
    replace_number = int(popsize*ps)       #将被复制的个体数，亦被淘汰的个体数


    #复制适应个体
    fit_value = []      #计算每个个体的适应度值
    for i in pop:
        fit_value.append(fit_function(i))

    fit_value_01 = []       #将适应度值0-1量纲化
    Min = min(fit_value)
    Max = max(fit_value)
    for i in fit_value:
        fit_value_01.append( (i-Min)/(Max-Min) )
    probe = np.cumsum(fit_value_01)
    replace_number_s = np.sort( 0.6*np.random.random(size=[replace_number,1]) )     #生成随机序列，随后用于和适应度值比较
    fit_pop = np.zeros(replace_number,dtype=np.int)

    #选择优秀个体
    j = 0
    for i in range(replace_number):
        while j < popsize:
            if probe[j] >= replace_number_s[i]:
                fit_pop[i] = pop[j]
                break
            else:
                j += 1


    u_fit_value = []
    for i in pop:
        u_fit_value.append(ufit_function(i))
    Max = max(u_fit_value)
    Min = min(u_fit_value)
    u_fit_value_01 = []
    for i in fit_value:
        u_fit_value_01.append( (Max-i)/(Max-Min) )
    prob = np.cumsum(u_fit_value_01)
    rns = np.sort( np.random.random(size=[replace_number,1])*0.8 + 0.2 )



    #替换劣质个体
    j = 1
    for i in range(replace_number):
        while j < popsize:
            if prob[j] > rns[i]:
                pop[j] = fit_pop[i]
                break
            else:
                j += 1

    return pop

