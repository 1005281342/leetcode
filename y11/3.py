from typing import List
from itertools import combinations


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        if not prob:
            return 0
        if target == 0:
            tmp = 1
            for i in prob:
                tmp *= (1 - i)
            return tmp
        prob = [i for i in prob if i > 0]
        if len(prob) < target:
            return 0

        ans = 0
        for x in combinations(prob, target):
            tp = prob[::]
            tmp = 1
            for i in x:
                tmp *= i
                # print(i, tp)
                tp.remove(i)
            # print(tmp)
            for j in tp:
                tmp *= (1-j)
            ans += tmp

        if ans > 1:
            return 0
        return ans
