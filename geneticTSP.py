# 일반 유전 알고리즘
import csv
import random

import Selection
from CalculationDist import Calculation
from MakeMutation import Mutation
from MakeCrossover import Crossover

class geneTSP:
    cities = []
    cities_idx = [[0 for i in range(1000)]for j in range(5)]

    '''
    cities_idx1 = []
    cities_idx2 = []
    cities_idx3 = []
    cities_idx4 = []
    cities_idx5 = []
    cities_idx6 = []
    cities_idx7 = []
    cities_idx8 = []
    cities_idx9 = []
    cities_idx10 = []
    '''

    def __init__(self):
        with open("TSP.csv", mode='r', newline='') as tsp:
            reader = csv.reader(tsp)
            for row in reader:
                self.cities.append(row)
        for i in range(5):
            for j in range(1000):
                self.cities_idx[i][j] = j
            random.shuffle(self.cities_idx[i])

        '''
        self.cities_idx[1] = self.cities_idx.copy()
        random.shuffle(self.cities_idx1)
        self.cities_idx[2] = self.cities_idx.copy()
        random.shuffle(self.cities_idx2)
        self.cities_idx3 = self.cities_idx.copy()
        random.shuffle(self.cities_idx3)
        self.cities_idx4 = self.cities_idx.copy()
        random.shuffle(self.cities_idx4)
        self.cities_idx5 = self.cities_idx.copy()
        random.shuffle(self.cities_idx5)
        self.cities_idx6 = self.cities_idx.copy()
        random.shuffle(self.cities_idx6)
        self.cities_idx7 = self.cities_idx.copy()
        random.shuffle(self.cities_idx7)
        self.cities_idx8 = self.cities_idx.copy()
        random.shuffle(self.cities_idx8)
        self.cities_idx9 = self.cities_idx.copy()
        random.shuffle(self.cities_idx9)
        self.cities_idx10 = self.cities_idx.copy()
        random.shuffle(self.cities_idx10)
        '''
    # 실제로 실행 담당하는 함수
    def execute(self):
        print("1    : " + str(Calculation.evalTotalcost(self.cities_idx[1], self.cities)))
        print("2    : " + str(Calculation.evalTotalcost(self.cities_idx[2], self.cities)))
        print("3    : " + str(Calculation.evalTotalcost(self.cities_idx[3], self.cities)))
        print("4    : " + str(Calculation.evalTotalcost(self.cities_idx[4], self.cities)))

        '''
        print("5    : " + str(Calculation.evalTotalcost(self.cities_idx5, self.cities)))
        print("6    : " + str(Calculation.evalTotalcost(self.cities_idx6, self.cities)))
        print("7    : " + str(Calculation.evalTotalcost(self.cities_idx7, self.cities)))
        print("8    : " + str(Calculation.evalTotalcost(self.cities_idx8, self.cities)))
        print("9    : " + str(Calculation.evalTotalcost(self.cities_idx9, self.cities)))
        print("10   : " + str(Calculation.evalTotalcost(self.cities_idx10, self.cities)))
        '''

        print("=============================================")

        #print(self.cities_idx2)
        print("교차 연산을 실행합니다.")
        #p = Crossover.order_cross(self.cities_idx1, self.cities_idx2)

        fitness = [0 for i in range(6)]
        fitnum = [[0 for i in range(2)] for j in range(6)]

        #모든 경우의 수의 fitness 탐색
        N = 4
        k = 0
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                fitness[k] = Calculation.calculate_fitness(self.cities_idx[i], self.cities, self.cities_idx[j], self.cities)
                fitnum[k] = [i, j]
                k += 1
        '''
        fitness[0] = Calculation.calculate_fitness(self.cities_idx1, self.cities, self.cities_idx2, self.cities)
        fitness[1] = Calculation.calculate_fitness(self.cities_idx1, self.cities, self.cities_idx3, self.cities)
        fitness[2] = Calculation.calculate_fitness(self.cities_idx1, self.cities, self.cities_idx4, self.cities)
        fitness[3] = Calculation.calculate_fitness(self.cities_idx2, self.cities, self.cities_idx3, self.cities)
        fitness[4] = Calculation.calculate_fitness(self.cities_idx2, self.cities, self.cities_idx4, self.cities)
        fitness[5] = Calculation.calculate_fitness(self.cities_idx3, self.cities, self.cities_idx4, self.cities)
        '''

        roulnum = Selection.Select.roulette_wheel(fitness)
        print("fitness = " + str(fitness))
        print("roulnum = " + str(roulnum))
        #print("fitnum  = " + str(fitnum))

        cities1 = fitnum[roulnum][0]
        cities2 = fitnum[roulnum][1]
        print("selected cities are " + str(cities1) + ", " + str(cities2))
        p = Crossover.order_cross(self.cities_idx[cities1], self.cities_idx[cities2])
        print(str(cities1) + "    : " + str(Calculation.evalTotalcost(self.cities_idx[cities1], self.cities)))
        print(str(cities2) + "    : " + str(Calculation.evalTotalcost(self.cities_idx[cities2], self.cities)))

        print(Calculation.evalTotalcost(p, self.cities))

        