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

    # 클래스 초기화
    def __init__(self, sol, gen):
        self.sol = sol
        self.gen = gen
        self.cities_idx = [[0 for _ in range(1000)] for _ in range(sol)]
        self.elite_cities_idx = [0 for _ in range(sol)]
        self.elite_fitness = [0 for _ in range(sol)]

        with open("TSP.csv", mode='r', newline='') as tsp:
            reader = csv.reader(tsp)
            for row in reader:
                self.cities.append(row)

        for i in range(1000):
            self.cities_idx_original.append(i)

        for i in range(self.sol):
            self.cities_idx[i] = self.cities_idx_original.copy()
            random.shuffle(self.cities_idx[i])

        # 초기 fitness 설정
        for i in range(self.sol):
            self.fitness.append(
                Calculation.calculate_fitness(self.cities, self.cities_idx_original, self.cities, self.cities_idx[i]))

    # 실제로 실행 담당하는 함수
    def execute(self, count):
        roulette_fit = []

        # roulette fitness
        for i in range(0, 10):
            roulette_fit.append(Calculation.roulette_fitness(self.fitness, i, 3))

        index = Select.roulette_wheel(roulette_fit)

        self.elite_fitness[0] = self.fitness[index[0]]
        if self.best_fitness == -1:
            self.best_fitness = self.elite_fitness[0]

        new_cities_idx = Crossover.order_cross(self.cities_idx[index[0]], self.cities_idx[index[1]])

        self.elite_cities_idx[count] = Mutation.randomMutate(new_cities_idx)
        self.elite_fitness[count] = Calculation.calculate_fitness(self.cities, self.cities_idx_original, self.cities, self.elite_cities_idx[count])

        if self.best_fitness > self.elite_fitness[count]:
            self.cities_idx[index[0]] = self.elite_cities_idx[count]
            self.best_fitness = self.elite_fitness[count]

    def evolution(self):
        evolarr = [0 for _ in range(self.sol)]

        # sol * gen
        for j in range(self.gen):
            for i in range(self.sol):
                self.execute(i)
                evolarr[i] = round(Calculation.evalTotalcost(self.elite_cities_idx[i], self.cities), 1)
            self.generation += 1

        # 마지막 세대 output
        print(self.elite_cities_idx[evolarr.index(min(evolarr))])       # 마지막 세대 solution
        #print(min(evolarr))                                             # 마지막 세대 dist

        return min(evolarr)


