from typing import List

from collections import Counter


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        d = Counter(nums)
        return d[target] > len(nums) / 2

if __name__ == '__main__':
    pass