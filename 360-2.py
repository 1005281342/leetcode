from typing import List
from collections import deque


class Solution:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None

    def f(self, num):
        if self.a is None or self.b is None or self.c is None:
            return 0
        return num ** 2 * self.a + num * self.b + self.c

    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        self.a = a
        self.b = b
        self.c = c

        if a == 0:
            if b > 0:
                return [self.f(num) for num in nums]
            else:
                return [self.f(num) for num in nums][::-1]

        index = b / (-2 * a)
        left = list()
        right = list()
        for num in nums:
            if num >= index:
                right.append(self.f(num))
            else:
                left.append(self.f(num))

        # print(left)
        # print(right)
        rsp = list()
        if a > 0:
            left = left[::-1]
        else:
            right = right[::-1]
        # print(left)
        # print(right)
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                rsp.append(left[i])
                i += 1
            else:
                rsp.append(right[j])
                j += 1

        tl = left[i:]
        if tl:
            if tl[-1] <= rsp[0]:
                rsp = tl + rsp
            elif tl[0] >= rsp[-1]:
                rsp.extend(tl)
        tr = right[j:]
        if tr:
            if tr[-1] <= rsp[0]:
                rsp = tr + rsp
            elif tr[0] >= rsp[-1]:
                rsp.extend(tr)

        return rsp


if __name__ == '__main__':

    S = Solution()
    S.sortTransformedArray([-100,-100,-89,-85,-82,-79,-75,-72,-69,-64,-62,-53,-41,-41,-40,-34,-28,-26,-26,-26,-25,-24,-19,-18,-11,-3,8,8,12,17,19,19,29,30,32,48,48,50,67,67,78,88,89,98]
,-96
,-49
,-35)