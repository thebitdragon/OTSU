# !/usr/bin/env python
# confing:utf-8 
__author__ = "liyanhe"

import time
time_start = time.time()    #开始计时
import numpy as np
from PIL import Image
from used_function import obj_function       #引入目标函数，otsu最大类间方差
from used_function import fit_function
from Evaluate import Evaluate
from Select import Select
from Crossover import Crossover
from Mutation import Mutation




#参数初始化
min_x_value = 0      #自变量x的下限值
max_x_value = 65535      #自变量x的上限值

popsize = 80      #种群大小
codelength = 16       #自变量的编码长度

max_GN_limitation = 20        #允许最大进化代数
df_max = 0.00001       #两代最优个体适应度差值绝对值的上限
less_df_n = 3        #两代最优个体适应度绝对值差值连续小于df_max的次数

ps = 0.99       #复制概率
pc = 0.3       #交叉概率
pm = 0.1       #变异概率

Tmin = 90     #退火下限温度
T = 100        #退火初始温度
r = 0.99        #退火快买因子

#种群初始化
pop = np.random.randint(min_x_value,(max_x_value - 1),size=[popsize,1])      #种群初始化

#变量初始化
GN = 0      #记录进化过程遗传代数
less_df_cnt = 0     #几率两代最优个体适应度差值连续小于上限的次数
best_code = Evaluate(pop)      #记录进化最优个体,初始化
history_best_code = np.zeros((max_GN_limitation,1),dtype=np.int)        #记录每一代最优个体
history_cut = 0     #记录最优个体数组‘history_best_code’的索引



#开始遗传迭代
while GN < max_GN_limitation:
    #执行遗传、交叉、变异操作，产生新种群
    pop = Select(pop,ps)
    pop = Crossover(pop,pc)
    pop = Mutation(pop,pm)

    current_beat_code = Evaluate(pop)       #记录当前种群最优个体
    #判断是否结束遗传过程
    if np.abs( fit_function(best_code) - fit_function(current_beat_code) ) < df_max:
        less_df_cnt += 1
    else:
        less_df_cnt = 0

    if less_df_cnt >= less_df_n:
        break

    #模拟退火
    #beat_code_move  最优个体轻微移动后的结果
    for i in range(2):
        best_code_move = current_beat_code + np.random.randint(-2,3)        #波动范围为-2~2
        de = fit_function(best_code_move) - fit_function(best_code)
        if  de >= 0:
            current_beat_code = best_code_move
        else:
            if np.e**(de/T) > float(np.random.random(1)):
                current_beat_code = best_code_move
        T = r*T


    #历史种群最优个体保留
    if fit_function(best_code) > fit_function(current_beat_code):
        M = np.random.randint(0,popsize)
        pop[M] = best_code
    else:
        best_code = current_beat_code
    history_best_code[history_cut] = best_code
    history_cut += 1

    GN += GN


#进化结束，得到结果
print(best_code)

time_end = time.time()  #结束计时
print("usetime:",time_end - time_start)

