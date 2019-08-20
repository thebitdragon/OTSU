# !/usr/bin/env python
# confing:utf-8 
__author__ = "liyanhe"



from used_function import fit_function
def Evaluate(pop):
    """

    :param pop:待评价种群
    :return: 最优个体的编码
    """
    pop_fitness_value = []
    for i in pop:
        pop_fitness_value.append(fit_function(i))
    Max = max(pop_fitness_value)
    M = pop_fitness_value.index(Max)        #纪录最大值的位置
    best_code = pop[M]
    return best_code


