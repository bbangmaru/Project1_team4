import numpy as np

class Calculation:
    # Euclidean distance measuring function
    @staticmethod
    def calculate_dist(x, y) :
        dist = np.linalg.norm(np.array(x)-np.array(y))
        return dist

    # 2. evaluate solution cost - 해집합의 최종 cost를 계산
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