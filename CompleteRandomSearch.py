import random
import time
import CalculationDist as cd


class CRS:
    # CompleteRandomSearch
    # shuffle solution and generate RandomSearch by 10secs
    @staticmethod
    def cost(s, c):
        final_cost = 99999
        now = time.time()
        while now + 10 > time.time():
            if final_cost > cd.Calculation.evalTotalcost(s, c):
                final_cost = cd.Calculation.evalTotalcost(s, c)
            random.shuffle(s)
        # best case of CompleteRandomSearch
        return final_cost


