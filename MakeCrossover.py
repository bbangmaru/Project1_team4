from email import header
import random
import numpy as np


class Crossover:
    @staticmethod
    def order_cross(origin_idx1, origin_idx2):
        length = len(origin_idx1)
        start_idx = random.randint(0, length - 1)
        end_idx = random.randint(start_idx + 1, length)
        ret = origin_idx1[start_idx : end_idx].copy()
        check = set() # 중복 제거
        # 방문 check
        for i in range(len(ret)):
            check.add(ret[i])
        # origin_idx2의 요소를 중복 없이 ret에 추가
        for i in range(length):
            if origin_idx2[i] not in check:
                check.add(origin_idx2[i])
                ret.append(origin_idx2[i])
        return ret

    @staticmethod
    def pmx(cities_idx1, cities_idx2):
        length = len(cities_idx1)
        start_idx = random.randint(0, length - 1)
        end_idx = random.randint(start_idx + 1, length)
        ret = np.concatenate((cities_idx2[:start_idx], cities_idx1[start_idx:end_idx], cities_idx2[end_idx:]), axis=0).astype(np.int32).tolist()
        
        flag = False
        while flag == False:
            flag = True
            # 앞 부분 비교
            compare1 = ret[start_idx:]
            for i in range(start_idx):
                if ret[i] in compare1: # 중복된 요소가 있는 경우
                    point = cities_idx1.index(ret[i]) # 해당 위치를 cities_idx1에서 찾아온다
                    ret[i] = cities_idx2[point] # 해당 위치에 해당하는 요소를 cities_idx2에서 찾아서 대입
                    flag = False

            # 뒷 부분 비교
            compare2 = ret[:end_idx]
            for i in range(end_idx, length):
                if ret[i] in compare2:
                    point = cities_idx1.index(ret[i])
                    ret[i] = cities_idx2[point]
                    flag = False
            
        return ret