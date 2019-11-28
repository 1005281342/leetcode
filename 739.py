from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stk = list()
        for i, v in enumerate(T):
            while stk and T[stk[-1]] < v:
                res[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
        return res


if __name__ == '__main__':
    S = Solution()
    x = S.dailyTemperatures([11, 22, 13, 22, 4, 56, 23])
    print(x)
