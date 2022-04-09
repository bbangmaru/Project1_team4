import random
from CalculationDist import Calculation


class Select:
    #랜덤으로 선택해주는 함수
    @staticmethod
    def randomSelect():
        
        return

    # roulette-wheel 선택
    @staticmethod
    def roulette_wheel(fitness):
        fitnessSum = 0
        idx = [-1, -1]
        for i in range(len(fitness)):
            fitnessSum += fitness[i]
        print("fitnessSum   : ", fitnessSum)

        point1 = random.uniform(0, fitnessSum)
        while point1 != fitnessSum:
            point1 = random.uniform(0, fitnessSum)

        while point1 > 0:
            idx[0] += 1
            point1 -= fitness[idx[0]]

        while 1:
            point2 = random.uniform(0, fitnessSum)
            while point2 > 0:
                idx[1] += 1
                point2 -= fitness[idx[1]]
            if idx[0] != idx[1]:
                print("idx          : ", idx)
                return idx



