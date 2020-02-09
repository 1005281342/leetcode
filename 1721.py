from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = list()
        for i, vs in enumerate(mat):
            ans.append((sum(vs), i))
        ans.sort()
        return [ans[i][1] for i in range(k)]
