from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        t = nums * 2

        res = [-1] * len(nums)
        for i, v in enumerate(nums):
            for j in range(i + 1, len(t)):
                if v < t[j]:
                    res[i] = t[j]
                    break

        return res

# 1 2 3 4 5 1 2 3 4 5