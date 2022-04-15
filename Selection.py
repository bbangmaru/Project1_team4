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
