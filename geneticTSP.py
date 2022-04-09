# 일반 유전 알고리즘
import csv
import random
from CalculationDist import Calculation
from MakeMutation import Mutation
from MakeCrossover import Crossover
from Selection import Select

class geneTSP:
    cities = []
    cities_idx = []
    # 해집단 10개
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
    fitness = []
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

        # 초기 fitness 설정
        self.fitness.append(Calculation.calculate_fitness(self.cities, self.cities_idx, self.cities, self.cities_idx1))
        self.fitness.append(Calculation.calculate_fitness(self.cities, self.cities_idx, self.cities, self.cities_idx2))
        self.fitness.append(Calculation.calculate_fitness(self.cities, self.cities_idx, self.cities, self.cities_idx3))
        self.fitness.append(Calculation.calculate_fitness(self.cities, self.cities_idx, self.cities, self.cities_idx4))
        self.fitness.append(Calculation.calculate_fitness(self.cities, self.cities_idx, self.cities, self.cities_idx5))
        self.fitness.append(Calculation.calculate_fitness(self.cities, self.cities_idx, self.cities, self.cities_idx6))
        self.fitness.append(Calculation.calculate_fitness(self.cities, self.cities_idx, self.cities, self.cities_idx7))
        self.fitness.append(Calculation.calculate_fitness(self.cities, self.cities_idx, self.cities, self.cities_idx8))
        self.fitness.append(Calculation.calculate_fitness(self.cities, self.cities_idx, self.cities, self.cities_idx9))
        self.fitness.append(Calculation.calculate_fitness(self.cities, self.cities_idx, self.cities, self.cities_idx10))
            
    
        
    # 실제로 실행 담당하는 함수
    def execute(self):
        print("=============================================")
        print("Calculate Fitness...")
        print("Selection Start...")
        for i in range(len(self.fitness)):
            print(i, ":", self.fitness[i])
        roulette_fit  = [] # roulette fitness
        for i in range(0, 10):
            roulette_fit.append(Calculation.roulette_fitness(self.fitness, i, 3))
        print(roulette_fit)
        index = Select.roulette_wheel(roulette_fit)
        print("index: ", index)
        print("Crossover Start...")
        new_cities_idx1 = Crossover.order_cross(self.cities_idx1, self.cities_idx2)
        Calculation.calculate_fitness(self.cities, self.cities_idx1, self.cities, self.cities_idx2)
        print("Mutation Start...")
        