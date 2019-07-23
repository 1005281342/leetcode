"""

    三数之和
    1. 排序
    2. 按顺序 固定一个值(这里选择从左到由)
"""
from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        length = len(nums)
        res = list()
        for k in range(length - 2):

            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            l = k + 1
            r = length - 1

            while l < r:
                ss = nums[l] + nums[r] + nums[k]
                if ss > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif ss < 0:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                else:
                    res.append([nums[k], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res


if __name__ == '__main__':
    S = Solution()
    res = S.threeSum(nums=[0,0,0])
    print(res)
