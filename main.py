import csv
import os
import numpy as np
import pandas as pd

from CompleteRandomSearch import CRS # 완전 무작위 탐색
from CalculationDist import Calculation # 계산 담당
from ClusteringCity import Clustering # 클러스터링 담당
from MakeCrossover import Crossover # 교차연산 담당
from MakeMutation import Mutation # 변이 담당
from Selection import Select # 선택 담당 - fitness 함수를 정의하면 됨
from Tree import TreeSearch # 트리 search 담당
import geneticTSP

df = pd.read_csv("TSP.csv", header=None, names=['x', 'y'])
#print(df)
cities = []
with open("TSP.csv", mode='r', newline='') as tsp:
    reader = csv.reader(tsp)
    for row in reader :
        cities.append(row)

sol = []

#1. get solution sequence and reordering (sort from 0)
with open("example_solution.csv", mode='r', newline='') as solution:
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


os.system("cls")
print("================================")
print("=        Genetic TSP           =")
print("=                              =")
print("=  Option Value                =")
print("=    1 : CompleteRandomSearch  =")
print("=    2 : GeneticTSP            =")
print("=    3 : GeneticTSP + tree     =")
print("=                              =")
print("================================")
print("Input option : ", end = '')

option = int(input())
if option == 1:
    print("wait for 10secs...")
    sol = CRS.shuffle(sol)
    print("final total : " + str(CRS.cost(sol, cities)))
    #print(sol)

elif option == 2:
    gTSP = geneticTSP.geneTSP(30, 50)
    result = gTSP.evolution()
    print(result)
    ''' 함수로 만들거 >>
    idx = sol.index(0)  # ?
    front = sol[idx:]  # ? ~ 1000
    back = sol[0:idx]  # 0 ~ ?
    sol = front + back  # 두개를 합침
    # expand 0 city(start) for simplicity, 간단하게 생각하기 위해 도시 0부터 시작하는 걸로!
    sol.append(int(0))
    '''

elif option == 3:
    print("Clustering...")
    kcluster = Clustering()
    k = 10
    center_city_coord, child_city_idx, child_city_coord = kcluster.clusterTSP(df, k, cities)
    print("Tree Searching...")
    picked = [0 for _ in range(k)]
    tree_search_cost, tree_search_path = TreeSearch.DFS(picked, center_city_coord, k, 0)
    print(tree_search_cost)
    print(tree_search_path)

'''
elif option == 0:
    idx = list(range(0, 200))
    c = cities[:200]
    #print(Calculation.idxarray(idx, c))
    idxArr = Calculation.idxarray(idx, c)
    #print(Calculation.distantarray(idxArr))
    f = open("sampleDistantArray.csv", 'w', newline='')
    wr = csv.writer(f)
    for row in range(len(idxArr) - 1):
        wr.writerow(Calculation.distantarray(idxArr)[row])
    f.close()
'''


"""
# kcluster instance 생성
kcluster = Clustering()
k = 10
center_city_coord, child_city_idx, child_city_coord = kcluster.clusterTSP(df, k, cities)
picked = [0 for _ in range(k)]
tree_search_cost, tree_search_path = TreeSearch.DFS(picked, center_city_coord, k, 0)
print(tree_search_cost)
print(tree_search_path)
"""





