import random
import time
import CalculationDist as cd


class CRS:
    # CompleteRandomSearch
    # shuffle solution but first
    @staticmethod
    def shuffle(s):
        s.reverse()
        first = s.pop()
        random.shuffle(s)
        s.append(first)
        s.reverse()
        return s

    # shuffle solution and generate RandomSearch by 10secs
    @staticmethod
    def cost(s, c):
        mintot = 99999
        now = time.time()
        while now + 10 > time.time():
            curtot = cd.Calculation.evalTotalcost(s, c)
            if curtot < mintot:
                mintot = curtot
        # best case of CompleteRandomSearch
        return mintot


