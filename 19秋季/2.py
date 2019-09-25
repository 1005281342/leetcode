from typing import List
import math


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        a, b = 1, cont.pop()
        for x in cont[::-1]:
            a, b = b, a + b * x
            # print(a, b)

            g = math.gcd(a, b)
            a //= g
            b //= g
        return [b, a]


if __name__ == '__main__':
    S = Solution()
    s = S.fraction([3, 2, 0, 2])
    print(s)