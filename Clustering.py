import numpy as np
import csv
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import random

cities = []
sol = []
order = []
# Euclidean distance measuring function
def distance(x, y):
    dist = np.linalg.norm(np.array(x)-np.array(y))
    return dist

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
# 3. evaluate solution cost
def evalcost(s, c):
    total_cost = 0
    for idx in range(len(s)-1):
        # get city positions
        pos_city_1 = [float(c[s[idx]][0]), float(c[s[idx]][1])]
        pos_city_2 = [float(c[s[idx+1]][0]), float(c[s[idx+1]][1])]
        # distance calculation
        dist = distance(pos_city_1, pos_city_2)
        #print(dist)
        # accumulation
        total_cost += dist
    return total_cost

# 여기까진 첨부 자료
# cluster 해주는 함수
def clusterTSP(key, df, k):# k는 군집의 수를 의미
    sub = KMeans(n_clusters=k) # k개의 집단으로 분할
    sub.fit(df) # fit 시키기 - clustering 진행
    labels = sub.predict(df) # df가 속해있는 각각의 sample의 가장 가까운 cluster 예측 -> 각각의 sample이 속해있는 index를 반환
    df["cluster"] = sub.labels_ # data frame에 cluster열 추가, 0~k-1까지의 인덱스 형태를 지님
    center = sub.cluster_centers_ # 10개의 center -> sub 생성시 생성, 2차원 ndarray 형태, 중심점은 평균값
    # 중심점과, 자식 도시들을 head와 child에 추가
    head_city = center # 중심점 저장
    child_idx = [] # 중심 주변의 군집화된 도시 index
    child_city = [] # 군집화된 자식 도시 목록
    for i in range(k): #0~9
        head = []
        child = []
        for x in df[df["cluster"] == i].index:
            head.append(x)
        child_idx.append(head) # 리스트 통째로 넣기
        for j in range(len(head)):
            child.append(cities[head[j]])
        child_city.append(child)
    # 산점도 그려보기
    
    if 'p' in key: # 처음 1000개의 도시에 대한 부모집단 나누기
        plt.scatter(df.x, df.y, c=labels, s=10, alpha=0.5) # c 값으로 각각의 sample이 속해있는 cluster index 별로 색상 나누기, labels에는 인덱스 저장되어 있음
        plt.scatter(center[:, 0], center[:, 1], color="RED", s=100, marker='*') # 별은 중심점을 의미
        plt.title("CITY CLUSTER")
        plt.show()
    elif 'c' in key:
        plt.scatter(df.x, df.y, c="BLACK", s=10, alpha=0.5) # c 값으로 각각의 sample이 속해있는 cluster index 별로 색상 나누기, labels에는 인덱스 저장되어 있음
        plt.scatter(center[:, 0], center[:, 1], color="RED", s=100, marker='*') # 별은 중심점을 의미
        plt.title("CHILD")
        plt.show()
    
    return head_city, child_idx, child_city