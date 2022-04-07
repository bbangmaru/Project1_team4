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
        for i in range(len(fitness)):
            fitnessSum += fitness[i]
        point = random.random() * fitnessSum
        s = 0
        for i in range(len(fitness)):
            s += fitness[i]
            if point < s :
                return i