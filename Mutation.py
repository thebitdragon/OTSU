# !/usr/bin/env python
# confing:utf-8 
__author__ = "liyanhe"

import numpy as np
def Mutation(pop,pm):

    popsize = len(pop)

    #对个体x进行变异
    def mutate(x):
        return np.bitwise_or(x,np.random.randint(0,256))


    #根据变异率对种群进行变异
    mutate_member = np.random.random(size=[popsize,1])
    for i in range(popsize):
        if mutate_member[i] < pm:
            pop[i] = mutate(pop[i])

    return pop

