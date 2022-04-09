# 일반 유전 알고리즘
import csv
import random
from CalculationDist import Calculation
from MakeMutation import Mutation
from MakeCrossover import Crossover
from Selection import Select


class geneTSP:
    cities = []
    cities_idx_ = []
    # 해집단 10개
    cities_idx = [[0 for i in range(1000)] for j in range(10)]
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
    fitness = []
    elite_cities_idx = []  # 유전 과정을 한번 거친 해집합에 대한 도시 정보
    elite_fitness = []  # 유전 과정을 한번 거친 해집합에 대한 fitness

    def __init__(self):
        with open("TSP.csv", mode='r', newline='') as tsp:
            reader = csv.reader(tsp)
            for row in reader:
                self.cities.append(row)
        for i in range(0, 1000):
            self.cities_idx_.append(i)
        self.cities_idx[0] = self.cities_idx_.copy()
        random.shuffle(self.cities_idx[0])
        self.cities_idx[1] = self.cities_idx_.copy()
        random.shuffle(self.cities_idx[1])
        self.cities_idx[2] = self.cities_idx_.copy()
        random.shuffle(self.cities_idx[2])
        self.cities_idx[3] = self.cities_idx_.copy()
        random.shuffle(self.cities_idx[3])
        self.cities_idx[4] = self.cities_idx_.copy()
        random.shuffle(self.cities_idx[4])
        self.cities_idx[5] = self.cities_idx_.copy()
        random.shuffle(self.cities_idx[5])
        self.cities_idx[6] = self.cities_idx_.copy()
        random.shuffle(self.cities_idx[6])
        self.cities_idx[7] = self.cities_idx_.copy()
        random.shuffle(self.cities_idx[7])
        self.cities_idx[8] = self.cities_idx_.copy()
        random.shuffle(self.cities_idx[8])
        self.cities_idx[9] = self.cities_idx_.copy()
        random.shuffle(self.cities_idx[9])

        '''
            self.cities_idx1 = self.cities_idx.copy()
            random.shuffle(self.cities_idx1)
            self.cities_idx2 = self.cities_idx.copy()
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

        # 초기 fitness 설정
        self.fitness.append(
            Calculation.calculate_fitness(self.cities, self.cities_idx_, self.cities, self.cities_idx[0]))
        self.fitness.append(
            Calculation.calculate_fitness(self.cities, self.cities_idx_, self.cities, self.cities_idx[1]))
        self.fitness.append(
            Calculation.calculate_fitness(self.cities, self.cities_idx_, self.cities, self.cities_idx[2]))
        self.fitness.append(
            Calculation.calculate_fitness(self.cities, self.cities_idx_, self.cities, self.cities_idx[3]))
        self.fitness.append(
            Calculation.calculate_fitness(self.cities, self.cities_idx_, self.cities, self.cities_idx[4]))
        self.fitness.append(
            Calculation.calculate_fitness(self.cities, self.cities_idx_, self.cities, self.cities_idx[5]))
        self.fitness.append(
            Calculation.calculate_fitness(self.cities, self.cities_idx_, self.cities, self.cities_idx[6]))
        self.fitness.append(
            Calculation.calculate_fitness(self.cities, self.cities_idx_, self.cities, self.cities_idx[7]))
        self.fitness.append(
            Calculation.calculate_fitness(self.cities, self.cities_idx_, self.cities, self.cities_idx[8]))
        self.fitness.append(
            Calculation.calculate_fitness(self.cities, self.cities_idx_, self.cities, self.cities_idx[9]))

    # 실제로 실행 담당하는 함수
    def execute(self):
        print("=============================================")
        print("Calculate Fitness...")
        print("Selection Start...")
        for i in range(len(self.fitness)):
            print(i, ":", self.fitness[i])
        roulette_fit = []
        # roulette fitness
        for i in range(0, 10):
            roulette_fit.append(Calculation.roulette_fitness(self.fitness, i, 3))
        print(roulette_fit)
        index = Select.roulette_wheel(roulette_fit)
        print("index: ", index)
        print("Crossover Start...")
        new_cities_idx1 = Crossover.order_cross(self.cities_idx[index[0]], self.cities_idx[index[1]])
        Calculation.calculate_fitness(self.cities, self.cities_idx[index[0]], self.cities, self.cities_idx[index[1]])
        print("Mutation Start...")
