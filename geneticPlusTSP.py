# 3. 트리 구조를 활용한 유전 알고리즘 구현 파일
from CalculationDist import Calculation # 계산 담당
from ClusteringCity import Clustering # 클러스터링 담당
from MakeCrossover import Crossover # 교차연산 담당
from MakeMutation import Mutation # 변이 담당
from Selection import Select # 선택 담당 - fitness 함수를 정의하면 됨
from Tree import TreeSearch # 트리 search 담당

import numpy as np
import pandas as pd
import random
import csv

class geneplusTSP():
    cities = []
    k = 0
    df = pd.read_csv("TSP.csv", header=None, names=['x', 'y'])
    def __init__(self, k):
        with open("TSP.csv", mode='r', newline='') as tsp:
            reader = csv.reader(tsp)
            for row in reader:
                self.cities.append(row)
        self.k = k
        
    def execute(self):
        # Clustering 시작
        kcluster = Clustering()
        center_city_coord, child_city_idx, child_city_coord = kcluster.clusterTSP(self.df, self.k, self.cities)
        picked = [0 for _ in range(self.k)]
        tree_search_cost, tree_search_path = TreeSearch.DFS(picked, center_city_coord, self.k, 0)
        print(tree_search_cost)
        print(tree_search_path)

        return