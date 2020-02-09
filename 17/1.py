from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = list()
        for i in range(0, len(nums) - 1, 2):
            ans += [nums[i]] * nums[i + 1]

        return ans
