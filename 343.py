from math import sqrt


class Solution:

    def ans(self, nums):
        ans = 1
        for num in nums:
            ans *= num
        return ans

    def integerBreak(self, n: int) -> int:

        b = int(sqrt(n))
        q = n - b ** 2
        nums = [b] * b
        nums2 = [1] * q
        if len(nums) < len(nums2):
            nums, nums2 = nums2, nums
        for i, num in enumerate(nums2):
            nums[i] += num

        return self.ans(nums)
