import random
import numpy as np


class Select:
    # roulette-wheel 선택
    @staticmethod
    def roulette_wheel(fitness):
        fitnessSum = 0
        idx = [-1, -1]
        for i in range(len(fitness)):
            fitnessSum += fitness[i]

        point1 = random.uniform(0, fitnessSum)
        while point1 == fitnessSum:
            point1 = random.uniform(0, fitnessSum)

        while point1 > 0:
            idx[0] += 1
            point1 -= fitness[idx[0]]

        while 1:
            idx[1] = -1
            point2 = random.uniform(0, fitnessSum)
            while point2 > 0:
                idx[1] += 1
                point2 -= fitness[idx[1]]

            if idx[0] != idx[1]:
                return idx


    # 토너먼트 선택
    @staticmethod
    def tournament(fitness):
        t = 0.7 # 기준
        point = random.random()
        select = False          # False = 나쁜 것
        if point < t:
            select = True       #T rue = 좋은 것
        gene_idx = np.random.choice(np.arange(len(fitness)), size=2, replace=False)
        return select, gene_idx
