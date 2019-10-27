from typing import List

D = dict()


class Solution:

    def cnt(self, num):
        cnt = bin(num).count('1')
        D[num] = cnt
        return cnt

    def countBits(self, num: int) -> List[int]:

        ans = [0] * (num + 1)
        for i in range(num + 1):
            if D.get(i) is not None:
                ans[i] = D[i]
                continue
            ans[i] = self.cnt(i)
        return ans
