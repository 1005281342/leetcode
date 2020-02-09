from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        ans = [0] * len(arr)

        dt = dict()
        for i, v in enumerate(sorted(list(set(arr)))):
            dt[v] = i + 1
        for j, vj in enumerate(arr):
            ans[j] = dt[vj]
        return ans
