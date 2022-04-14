# 일반 유전 알고리즘
import csv
import random
from CalculationDist import Calculation
from MakeMutation import Mutation
from MakeCrossover import Crossover
from Selection import Select


class geneTSP():
    generation = 1                  # 세대
    cities = []                     # 도시 좌표
    cities_idx_original = []        # 도시 인덱스
    sol = 0                         # 해집단 초기화
    gen = 0                         # 총세대 초기화
    cities_idx = []                 # 도시 인덱스 * 해집단 수만큼 선언
    best_fitness = -1               # best_fitness 초기값 설정
    fitness = []                    # fitness
    elite_cities_idx = []           # 유전 과정을 한번 거친 해집합에 대한 도시 정보
    elite_fitness = []              # 유전 과정을 한번 거친 해집합에 대한 fitness
    citynum = 0
    cross = 'pmx'

    # 클래스 초기화
    def __init__(self, sol, gen, child_cities_idx, cross):
        if child_cities_idx == None:  # option 2
            self.sol = sol
            self.gen = gen
            self.cities_idx = [[0 for _ in range(1000)] for _ in range(sol)]
            self.elite_cities_idx = [0 for _ in range(sol)]
            self.elite_fitness = [0 for _ in range(sol)]
            self.cities_idx_original = [0 for _ in range(1000)]
            self.fitness = [0 for _ in range(sol)]
            self.cross = cross

            with open("TSP.csv", mode='r', newline='') as tsp:
                reader = csv.reader(tsp)
                for row in reader:
                    self.cities.append(row)

            for i in range(1000):
                self.cities_idx_original[i] = i

            for i in range(self.sol):
                self.cities_idx[i] = self.cities_idx_original.copy()
                random.shuffle(self.cities_idx[i])

            # 초기 fitness 설정
            for i in range(self.sol):
                self.fitness[i] = Calculation.calculate_fitness(self.cities, self.cities_idx_original, self.cities, self.cities_idx[i])
        
        else:
            self.sol = sol
            self.gen = gen
            self.citynum = len(child_cities_idx)
            self.cities_idx = [[0 for _ in range(self.citynum)] for _ in range(sol)]
            self.elite_cities_idx = [0 for _ in range(sol)]
            self.elite_fitness = [0 for _ in range(sol)]
            self.cities_idx_original = [0 for _ in range(self.citynum)]
            self.fitness = [0 for _ in range(sol)]
            self.cross = cross
            with open("TSP.csv", mode='r', newline='') as tsp:
                reader = csv.reader(tsp)
                for row in reader:
                    self.cities.append(row)

            self.cities_idx_original = child_cities_idx.copy()

            for i in range(self.sol):
                self.cities_idx[i] = self.cities_idx_original.copy()
                random.shuffle(self.cities_idx[i])

            # 초기 fitness 설정
            for i in range(self.sol):
                self.fitness[i] = Calculation.calculate_fitness(self.cities, self.cities_idx_original, self.cities, self.cities_idx[i])

    # 실제로 실행 담당하는 함수1 - 룰렛 휠 선택, 순서 교차 사용
    def execute1(self, count):
        roulette_fit = [0 for _ in range(self.sol)]

        # roulette fitness
        for i in range(0, self.sol):
            roulette_fit[i] = Calculation.roulette_fitness(self.fitness, i, 3)

        index = Select.roulette_wheel(roulette_fit)

        self.elite_fitness[0] = self.fitness[index[0]]
        if self.best_fitness == -1:
            self.best_fitness = self.elite_fitness[0]

        # CrossOver - order cross
        new_cities_idx = Crossover.order_cross(self.cities_idx[index[0]], self.cities_idx[index[1]])

        #Mutation
        self.elite_cities_idx[count] = Mutation.randomMutate(new_cities_idx)
        self.elite_fitness[count] = Calculation.calculate_fitness(self.cities, self.cities_idx_original, self.cities, self.elite_cities_idx[count])

        if self.best_fitness > self.elite_fitness[count]:
            self.cities_idx[index[0]] = self.elite_cities_idx[count]
            self.best_fitness = self.elite_fitness[count]

    # 실제로 실행 담당하는 함수2 - pmx 교차 연산 사용
    def execute2(self, count):
        roulette_fit = [0 for _ in range(self.sol)]

        # roulette fitness
        for i in range(0, self.sol):
            roulette_fit[i] = Calculation.roulette_fitness(self.fitness, i, 3)

        index = Select.roulette_wheel(roulette_fit)

        self.elite_fitness[0] = self.fitness[index[0]]
        if self.best_fitness == -1:
            self.best_fitness = self.elite_fitness[0]

        # CrossOver - pmx
        new_cities_idx = Crossover.pmx(self.cities_idx[index[0]], self.cities_idx[index[1]])

        #Mutation
        self.elite_cities_idx[count] = Mutation.randomMutate(new_cities_idx)
        self.elite_fitness[count] = Calculation.calculate_fitness(self.cities, self.cities_idx_original, self.cities, self.elite_cities_idx[count])

        if self.best_fitness > self.elite_fitness[count]:
            self.cities_idx[index[0]] = self.elite_cities_idx[count]
            self.best_fitness = self.elite_fitness[count]

    def evolution(self):
        evolarr = [0 for _ in range(self.sol)]

        # sol * gen
        if self.cross == 'order':
            for _ in range(self.gen):
                for i in range(self.sol):
                    self.execute1(i)
                    evolarr[i] = round(Calculation.evalTotalcost(self.elite_cities_idx[i], self.cities), 1)
                self.generation += 1

        elif self.cross == 'pmx':
            for _ in range(self.gen):
                for i in range(self.sol):
                    self.execute2(i)
                    evolarr[i] = round(Calculation.evalTotalcost(self.elite_cities_idx[i], self.cities), 1)
                self.generation += 1

        return self.elite_cities_idx[evolarr.index(min(evolarr))], min(evolarr)


