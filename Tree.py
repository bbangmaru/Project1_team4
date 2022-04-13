from CalculationDist import Calculation


class TreeSearch:
    # backtracking DFS?
    @staticmethod
    def DFS(picked, center_city_coord, k, depth): #중앙지점 도시 index, 중앙지점 도시 좌표, 클러스터링 개수, 탐색할 depth
        if depth == k - 1:
            return Calculation.evalTotalcost(picked, center_city_coord), picked
        min_cost = 99999999
        min_path = []
        for i in range(0, k):
            if i not in picked:
                picked[depth] = i
                cost, pick = TreeSearch.DFS(picked, center_city_coord, k, depth + 1)
                if min_cost > cost:     # min_cost update하고 해당 경로 저장
                    min_cost = cost
                    min_path = pick.copy()
                picked[depth] = 0 
        return min_cost, min_path