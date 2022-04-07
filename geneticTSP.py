# 일반 유전 알고리즘
import csv
import random
from CalculationDist import Calculation
from MakeMutation import Mutation
from MakeCrossover import Crossover

class geneTSP:
    cities = []
    cities_idx = []
    cities_idx1 = []
    cities_idx2 = []
    cities_idx3 = []
    cities_idx4 = []
    cities_idx5 = []
    def __init__(self):
        with open("TSP.csv", mode='r', newline='') as tsp:
            reader = csv.reader(tsp)
            for row in reader :
                self.cities.append(row)
        for i in range(0, 1000):
            self.cities_idx.append(i)
        self.cities_idx1 = self.cities_idx.copy()
        random.shuffle(self.cities_idx1)
        self.cities_idx2 = self.cities_idx.copy()
        random.shuffle(self.cities_idx2)
    
        
    # 실제로 실행 담당하는 함수
    def execute(self):
        print(self.cities_idx1)
        print("=============================================")
        print(self.cities_idx2)
        print("교차 연산을 실행합니다.")
        p = Crossover.order_cross(self.cities_idx1, self.cities_idx2)
        print(p)
        