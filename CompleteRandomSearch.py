import numpy as np
import csv
import random
import time

# given cities
cities = []
# solution
sol = []

#1. get solution sequence and reordering (sort from 0)
with open('example_solution.csv', mode='r', newline='') as solution:
    # read solution sequence
    reader = csv.reader(solution)
    for row in reader:
        sol.append(int(row[0]))
    # reordering solution sequence, 해답 sequence를 재배치
    idx = sol.index(0) # 189

    front = sol[idx:] # 189 ~ 1000

    back = sol[0:idx] # 0 ~ 189

    sol = front + back # 두개를 합침
    # expand 0 city(start) for simplicity, 간단하게 생각하기 위해 도시 0부터 시작하는 걸로!
    sol.append(int(0))
# 2. get TSP city map
with open('TSP.csv', mode='r', newline='') as tsp:
    # read TSP city map
    reader = csv.reader(tsp)
    for row in reader:
        cities.append(row)

# 3. CompleteRandomSearch
# shuffle solution but first
def randsol(s):
    s.reverse()
    first = s.pop()
    random.shuffle(s)
    s.append(first)
    s.reverse()
    return s


class Calculation:
    # Euclidean distance measuring function
    @staticmethod
    def calculate_dist(x, y):
        dist = np.linalg.norm(np.array(x)-np.array(y))
        return dist

    # 3. evaluate solution cost - 해집합의 최종 cost를 계산
    @staticmethod
    def evalTotalcost(s, c):
        total_cost = 0
        for idx in range(len(s)-1):
            # get city positions
            pos_city_1 = [float(c[s[idx]][0]), float(c[s[idx]][1])]
            pos_city_2 = [float(c[s[idx+1]][0]), float(c[s[idx+1]][1])]
            # distance calculation
            dist = Calculation.calculate_dist(pos_city_1, pos_city_2)
            # accumulation
            total_cost += dist
        return total_cost

# shuffle solution and generate RandomSearch by 10secs
minTot = 99999
now = time.time()
while now + 10 > time.time():
    curTot = Calculation.evalTotalcost(randsol(sol), cities)
    if curTot < minTot:
        minTot = curTot

# best case of CompleteRandomSearch
print("final cost : " + str(minTot))
