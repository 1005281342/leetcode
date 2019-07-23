class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()

        length = len(nums)
        res = list()

        for p in range(length - 3):

            for k in range(p + 1, length - 2):

                l = k + 1
                r = length - 1

                while l < r:
                    ss = nums[l] + nums[r] + nums[k] + nums[p]
                    if ss - target > 0:
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif ss - target < 0:
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    else:
                        res.append([nums[p], nums[k], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.fourSum(nums=[0, 0, 0, 0], target=0))
