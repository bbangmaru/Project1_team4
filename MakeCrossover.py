from email import header
import random


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
