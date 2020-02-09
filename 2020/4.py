from typing import List


class Solution:
    def otaku(self, nums: List[int]) -> bool:

        for i, num in enumerate(nums[:len(nums)-1]):
            if num == 0 and nums[i+1] > 0:
                return True
        return False

