from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:

        ans = [1] * len(S)
        tc = list()
        for i, c in enumerate(S):
            if c == C:
                ans[i] = 0
                tc.append(i)
        for i, c in enumerate(S):
            ans[i] = min([abs(t - i) for t in tc])
        return ans