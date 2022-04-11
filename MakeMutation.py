import random
import numpy as np
class Mutation:
    # 단순 swap
    @staticmethod
    def randomMutate(cities_idx):
        idx = np.random.choice(cities_idx, size=2, replace=False)
        first = cities_idx.index(idx[0])
        second = cities_idx.index(idx[1])
        cities_idx[first], cities_idx[second] = cities_idx[second], cities_idx[first]
        return cities_idx