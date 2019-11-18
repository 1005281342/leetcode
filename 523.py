from typing import List


class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        if len(nums) == 2:
            return sum(nums) == k or (k!=0 and sum(nums)%k==0)
        st = 0
        d = {0: -1}
        for i, v in enumerate(nums):
            st += v
            if k != 0:
                st %= k
            if d.get(st) is not None:
                if i - d[st] > 1:
                    return True
            else:
                d[st] = i
        return False


    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    #
    #     if len(nums) <= 1:
    #         return False
    #     # 前缀和
    #     ta = [nums[0]] * len(nums)
    #     for i in range(1, len(nums)):
    #         ta[i] = nums[i] + ta[i-1]
    #
    #     for i in range(len(nums)-1):
    #         for j in range(1, len(nums)):
    #             t = ta[j] - ta[i] + nums[i]
    #             if t == k or (k != 0 and not t % k):
    #                 return True
    #
    #     return False
