from typing import List
from math import gcd


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        t = 0
        for num in nums:
            t = gcd(t, num)

        return t == 1
