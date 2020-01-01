from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n <= 1:
            return [0] * n
        x = [i for i in range(1, n // 2 + 1)]
        y = sorted([-i for i in x])
        if n % 2:
            return y + [0] + x

        return y + x