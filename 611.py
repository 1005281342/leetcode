from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        cnt = 0
        for i in range(len(nums) - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    cnt += right - left
                    right += 1
                else:
                    left += 1
        return cnt
