from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        for i, n in enumerate(nums):
            cnt += self.twoSumSmaller(nums, i + 1, target - n)
        return cnt

    def twoSumSmaller(self, nums: List[int], si, target: int) -> int:
        cnt = 0
        a = si
        b = len(nums) - 1
        while a < b:
            if nums[a] + nums[b] >= target:
                b -= 1
            else:
                cnt += b - a
                a += 1
        return cnt


if __name__ == '__main__':
    S = Solution()
    res = S.threeSumSmaller([-2, 0, 1, 3], 2)
    print(res)
