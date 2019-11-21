from typing import List
from math import inf


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return -inf
        sn = set(nums)
        t = -inf
        for n in sn:
            if n > t:
                t = n
        if len(sn) < 3:
            return t

        p = t
        t = -inf
        for n in sn:
            if n > t and n != p:
                t = n

        q = t
        t = -inf
        for n in sn:
            if n > t and n != p and n != q:
                t = n
        return t
