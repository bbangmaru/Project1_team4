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
        idx = 0
        for i in range(len(fitness)):
            fitnessSum += fitness[i]
        print("fitnessSum: ", fitnessSum)
        point = random.uniform(0, fitnessSum)
        print("point: ", point)
        while point > 0:
            point -= fitness[idx]
            idx += 1
        idx -= 1
        return idx

