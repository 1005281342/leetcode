from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:

        length = len(calories)

        res = 0
        for i in range(0, length - k + 1):

            st = sum(calories[i:i + k])
            # print(st)
            if st > upper:
                res += 1
            elif st < lower:
                res -= 1
            # print(res)

        return res


if __name__ == '__main__':
    S = Solution()
    print(S.dietPlanPerformance(calories=[1, 2, 3, 4, 5], k=1, lower=3, upper=3))
    print(S.dietPlanPerformance(calories=[3, 2], k=2, lower=0, upper=1))
    print(S.dietPlanPerformance(calories=[6, 5, 0, 0], k=2, lower=1, upper=5))
