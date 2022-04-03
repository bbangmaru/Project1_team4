import csv
import numpy as np
import pandas as pd

from CalculationDist import Calculation # 계산 담당
from ClusteringCity import Clustering # 클러스터링 담당
from MakeCrossover import Crossover # 교차연산 담당
from MakeMutation import Mutation # 변이 담당
from Selection import Select # 선택 담당 - fitness 함수를 정의하면 됨
from Tree import TreeSearch # 트리 search 담당

df = pd.read_csv("TSP.csv", header=None, names=['x', 'y'])
#print(df)
cities = []
with open('TSP.csv', mode='r', newline='') as tsp:
    reader = csv.reader(tsp)
    for row in reader :
        cities.append(row)
# kcluster instance 생성
kcluster = Clustering()
k = 10
center_city_coord, child_city_idx, child_city_coord = kcluster.clusterTSP(df, k, cities)
picked = [0 for _ in range(k)]
tree_search_cost, tree_search_path = TreeSearch.DFS(picked, center_city_coord, k, 0)
print(tree_search_cost)
print(tree_search_path)





