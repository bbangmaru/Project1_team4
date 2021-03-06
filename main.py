import csv
import os
import pandas as pd
import click
import time
import math

from CompleteRandomSearch import CRS # 완전 무작위 탐색
from CalculationDist import Calculation # 계산 담당
import geneticTSP
import geneticPlusTSP
import matplotlib.pyplot as plt

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
@click.option('--option',   type=click.INT,     help='1=Random | '
                                                     '2=Genetic TSP | '
                                                     '3=Genetic TSP with Tree Search',   default=1)
@click.option('--k',        type=click.INT,     help='number of Clusters',               default=10)
@click.option('--s',        type=click.INT,     help='number of Solution Groups',        default=10)
@click.option('--g',        type=click.INT,     help='number of Generations',            default=1000)
@click.option('--c',        type=click.STRING,  help='Crossover method : '
                                                     'pmx || order',                      default='pmx')
def main(option, k, s, g, c):
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
    if option == 1:
        print("================================")
        print("=    Complete Random Search    =")
        print("================================")
        start = time.time()
        print("final total : " + str(CRS.cost(sol, cities)))
        end = time.time()
        print("execution time : " + str(end - start))

    elif option == 2:
        print("================================")
        print("=          Genetic TSP         =")
        print("=        sol : " + str(s) + "              =")
        print("=        gen : " + str(g) + "            =")
        if c == 'pmx':
            print("=      cross : PMX             =")
        elif c == 'order':
            print("=      cross : Order           =")
        print("================================")

        start = time.time()
        gTSP = geneticTSP.geneTSP(s, g, None, c)  # 해집단 수, 세대 수, 도시 개수
        sol_idx, result = gTSP.evolution()
        sol_idx = finalManipulate(sol_idx)
        print("final total : " + str(Calculation.evalTotalcost(sol_idx, cities)))
        end = time.time()
        print("execution time : " + str(end - start))

        # 경로 시각화
        final_coord = [0 for _ in range(1001)]
        for i in range(len(sol_idx)):
            final_coord[i] = cities[sol_idx[i]]
        
        x = [0 for _ in range(1001)]
        y = [0 for _ in range(1001)]

        for i in range(1001):
            x[i] = (float)(final_coord[i][0])
            y[i] = (float)(final_coord[i][1])
            x[i] = round(x[i], 4)
            y[i] = round(y[i], 4)
        
        plt.figure(figsize=(100, 100))
        #plt.scatter(x, y, c='green')
        plt.scatter(x[0], y[0], s=200, c='blue') #시작점
        plt.plot(x, y, color='orange', marker='d', alpha=0.7)
        plt.show()
        plt.close()

    elif option == 3:
        print("================================")
        print("= Genetic TSP with Tree Search =")
        print("=          k : " + str(k) + "              =")
        print("=        sol : " + str(s) + "              =")
        print("=        gen : " + str(g) + "            =")
        if c == 'pmx':
            print("=      cross : PMX             =")
        elif c == 'order':
            print("=      cross : Order           =")
        print("================================")

        start = time.time()
        gplusTSP = geneticPlusTSP.geneplusTSP(k, s, g, c)  # 군집 개수, 해집단 수, 세대 수
        final_path = gplusTSP.execute()
        final_path = finalManipulate(final_path)
        print("final total : " + str(Calculation.evalTotalcost(final_path, cities)))
        end = time.time()
        print("execution time : " + str(end - start))

        # 경로 시각화
        final_coord = [0 for _ in range(1001)]
        for i in range(len(final_path)):
            final_coord[i] = cities[final_path[i]]
        
        x = [0 for _ in range(1001)]
        y = [0 for _ in range(1001)]

        for i in range(1001):
            x[i] = (float)(final_coord[i][0])
            y[i] = (float)(final_coord[i][1])
            x[i] = round(x[i], 4)
            y[i] = round(y[i], 4)
        
        plt.figure(figsize=(100, 100))
        plt.scatter(x, y, c='green')
        plt.scatter(x[0], y[0], s=200, c='blue') #시작점
        plt.plot(x, y, color='red')
        plt.show()
        plt.close()

        # csv 파일로 내보내기 0 ~ 999 ~ 0
        temp = pd.DataFrame(final_path)
        temp.iloc[:1000].to_csv('./solution_04' + str(Calculation.evalTotalcost(final_path, cities)) + '.csv', index=False, header=False)



if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
