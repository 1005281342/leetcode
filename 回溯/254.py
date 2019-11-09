from typing import List
from itertools import combinations


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        yz = list()
        while n // 5 == n / 5 and n > 1:
            yz.append(5)
            n //= 5

        while n // 3 == n / 3 and n > 1:
            yz.append(3)
            n //= 3

        while n // 2 == n / 2 and n > 1:
            yz.append(2)
            n //= 2

        if n > 1:
            yz.append(n)

        if len(yz) <= 1:
            return []
        if len(yz) == 2:
            return [yz, ]

        """
        回溯
        """


if __name__ == '__main__':
    S = Solution()
    S.getFactors(32)
