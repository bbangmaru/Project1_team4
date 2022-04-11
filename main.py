import csv
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import click

from CompleteRandomSearch import CRS # 완전 무작위 탐색
from CalculationDist import Calculation # 계산 담당
from ClusteringCity import Clustering # 클러스터링 담당
from MakeCrossover import Crossover # 교차연산 담당
from MakeMutation import Mutation # 변이 담당
from Selection import Select # 선택 담당 - fitness 함수를 정의하면 됨
from Tree import TreeSearch # 트리 search 담당
import geneticTSP
import geneticPlusTSP


def finalManipulate(final_path):
    # reordering solution sequence, 해답 sequence를 재배치
    idx = final_path.index(0) # 189

    front = final_path[idx:] # 189 ~ 1000

    back = final_path[0:idx] # 0 ~ 189

    final_path = front + back # 두개를 합침
    # expand 0 city(start) for simplicity, 간단하게 생각하기 위해 도시 0부터 시작하는 걸로!
    final_path.append(int(0))

    return final_path


@click.command()
@click.option('--option',   type=click.INT, help='1=Random | 2=Genetic TSP | 3=Genetic TSP with Tree Search', default=1)
def main(option):
    df = pd.read_csv("TSP.csv", header=None, names=['x', 'y'])
    # print(df)
    cities = []
    with open("TSP.csv", mode='r', newline='') as tsp:
        reader = csv.reader(tsp)
        for row in reader:
            cities.append(row)

    sol = []
    with open('example_solution.csv', mode='r', newline='') as solution:
        reader = csv.reader(solution)
        for row in reader:
            sol.append(int(row[0]))
        idx = sol.index(0)  # 189

        front = sol[idx:]  # 189 ~ 1000

        back = sol[0:idx]  # 0 ~ 189

        sol = front + back  # 두개를 합침
        # expand 0 city(start) for simplicity, 간단하게 생각하기 위해 도시 0부터 시작하는 걸로!
        sol.append(int(0))

    os.system("cls")
    #  option = int(input())
    if option == 1:
        print("================================")
        print("=    Complete Random Search    =")
        print("================================")
        print("wait for 10secs...")
        sol = CRS.shuffle(sol)
        print("final total : " + str(CRS.cost(sol, cities)))

    elif option == 2:
        print("================================")
        print("=          Genetic TSP         =")
        print("================================")

        gTSP = geneticTSP.geneTSP(10, 1000, None)  # 반복 횟수, 세대 횟수, 도시 개수
        sol_idx, result = gTSP.evolution()
        sol_idx = finalManipulate(sol_idx)
        # print(sol_idx)
        print("final total : " + str(Calculation.evalTotalcost(sol_idx, cities)))

    elif option == 3:
        print("================================")
        print("= Genetic TSP with Tree Search =")
        print("================================")

        k = 10  # 군집화 개수
        gplusTSP = geneticPlusTSP.geneplusTSP(k, 20, 100)  # 군집 개수, 해집단 개수, 세대 수
        final_path = gplusTSP.execute()
        final_path = finalManipulate(final_path)
        # print(final_path)
        print("final total : " + str(Calculation.evalTotalcost(final_path, cities)))


if __name__ == "__main__":
    main() # pylint: disable=no-value-for-parameter
