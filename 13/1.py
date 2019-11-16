from typing import List
from math import log2


class Solution:
    def encode(self, num: int) -> str:
        if not num:
            return ""

        t = int(log2(num + 1))
        # print(t)
        xd = 2 ** t - 1
        d = bin(num - xd)[2:]
        return (t - len(d)) * "0" + d


if __name__ == '__main__':
    S = Solution()
    print(S.encode(2))
    print(S.encode(3))
    print(S.encode(6))
    print(S.encode(7))
