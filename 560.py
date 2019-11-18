from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cnt = nums.count(k)

        st = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            st[i] = st[i - 1] + nums[i]

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if st[j] - st[i] + nums[i] == k:
                    cnt += 1

        return cnt


