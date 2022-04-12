import numpy as np

class Calculation:
    # Euclidean distance measuring function
    @staticmethod
    def calculate_dist(x, y) :
        dist = np.linalg.norm(np.array(x)-np.array(y))
        return dist

    # evaluate solution cost - 해집합의 최종 cost를 계산
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

    @staticmethod
    def roulette_fitness(fitness, cur_idx, k):
        best = min(fitness)
        worst = max(fitness)
        cur = fitness[cur_idx]
        fit = (worst - cur) + (worst - best) / (k - 1)
        return fit
    # fitness calculation - 적합도 계산
    @staticmethod
    def calculate_fitness(original_cities, original_cities_idx, new_cities, new_cities_idx): #원래 city index, 좌표 & 바뀐 city index, 좌표
        original_dist = Calculation.evalTotalcost(original_cities_idx, original_cities)
        new_dist = Calculation.evalTotalcost(new_cities_idx, new_cities)
        fit = new_dist / original_dist
        return fit
