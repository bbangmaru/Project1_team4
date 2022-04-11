from CalculationDist import Calculation

class TreeSearch:
    # backtracking DFS?
    @staticmethod
    def DFS(picked, center_city_coord, k, depth): #중앙지점 도시 index, 중앙지점 도시 좌표, 클러스터링 개수, 탐색할 depth
        if depth == k - 1: # leaf 도달시 해 구했으므로 경로 길이 & 경로 반환 
            return Calculation.evalTotalcost(picked, center_city_coord), picked
        min_cost = 99999999
        min_path = []
        for i in range(0, k):
            if i not in picked:
                picked[depth] = i
                cost, pick = TreeSearch.DFS(picked, center_city_coord, k, depth + 1) # 재귀호출로 depth 1씩 증가시키며 DFS 구현
                if min_cost > cost: # min_cost update하고 해당 경로 저장
                    min_cost = cost
                    min_path = pick.copy()
                picked[depth] = 0 # 다시 0으로 만들어주기
        return min_cost, min_path