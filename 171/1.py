from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        if n == 2:
            return [1, 1]

        for i in range(1, (n + 1) // 2 + 1):
            if "0" in str(i) + str(n - i):
                continue
            else:
                return [i, n - i]
