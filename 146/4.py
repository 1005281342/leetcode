from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:

        sign = (-1, 1)
        res = 0
        for a in sign:
            for b in sign:
                nums = [0]
                for i in range(len(arr1)):
                    nums.append(a * arr1[i] + b * arr2[i] + i)
                res = max(res, max(nums) - min(nums))

        return res


if __name__ == '__main__':
    S = Solution()
    r = S.maxAbsValExpr(arr1=[1, 2, 3, 4], arr2=[-1, 4, 5, 6])
    print(r)
