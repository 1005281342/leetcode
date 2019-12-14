from typing import List
from itertools import combinations

tmp = [[[0, 0], [0, 1], [0, 2]],
       [[1, 0], [1, 1], [1, 2]],
       [[2, 0], [2, 1], [2, 2]],
       [[0, 0], [1, 0], [2, 0]],
       [[0, 1], [1, 1], [2, 1]],
       [[0, 2], [1, 2], [2, 2]],
       [[0, 0], [1, 1], [2, 2]],
       [[0, 2], [1, 1], [2, 0]],]


class Solution:

    def helper(self, v):
        if len(v) < 3:
            return False
        v = tuple(x for x in v)
        print(v)
        for vv in tmp:
            for c in combinations(v, 3):
                if sorted(tuple(c)) == sorted(vv):
                    return True
        return False

    def tictactoe(self, moves) -> str:

        if len(moves) <= 4:
            return "Pending"

        x = list()
        o = list()

        for i, v in enumerate(moves):
            if not (i % 2):
                x.append(v)
                if self.helper(x):
                    return "A"
            else:
                o.append(v)
                if self.helper(o):
                    return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"

