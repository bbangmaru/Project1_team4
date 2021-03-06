from ClusteringCity import Clustering # 클러스터링 담당
from Tree import TreeSearch # 트리 search 담당
import geneticTSP
import pandas as pd
import csv

class geneplusTSP():
    cities = []
    k = 0
    sol = 0
    gen = 0
    cross = 'pmx'
    df = pd.read_csv("TSP.csv", header=None, names=['x', 'y'])

    def __init__(self, k, sol, gen, cross):
        with open("TSP.csv", mode='r', newline='') as tsp:
            reader = csv.reader(tsp)
            for row in reader:
                self.cities.append(row)
        self.k = k
        self.sol = sol
        self.gen = gen
        self.cross = cross
        
    def execute(self):
        # Clustering 시작
        kcluster = Clustering()
        center_city_coord, child_city_idx = kcluster.clusterTSP(self.df, self.k)

        rets = []
        sol_path = []
        for i in range(self.k):
            g = geneticTSP.geneTSP(self.k, self.gen, child_city_idx[i], self.cross)
            sol, ret = g.evolution()
            rets.append(ret)
            sol_path.append(sol)

        picked = [0 for _ in range(self.k)]
        tree_search_cost, tree_search_path = TreeSearch.DFS(picked, center_city_coord, self.k, 0)

        final_path = []
        for i in range(self.k):
            idx = tree_search_path[i]
            temp = sol_path[idx]
            for j in range(len(temp)):
                final_path.append(temp[j])

        return final_path