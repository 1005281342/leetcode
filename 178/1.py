from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        a = sorted(nums)
        d = dict()
        for i, v in enumerate(a):
            if d.get(v) is None:
                d[v] = i
        ans = [0] * len(nums)
        for i, v in enumerate(nums):
            ans[i] = d[v]
        return ans


if __name__ == '__main__':

    S = Solution()
    S.smallerNumbersThanCurrent([7,7,7])