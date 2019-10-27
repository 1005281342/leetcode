"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
from typing import List


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        pass


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:

        ans = list()
        ff = customfunction.f
        for i in range(1, z+1):
            for j in range(1, z+1):
                d = ff(i, j)
                if d == z:
                    ans.append([i, j])
                elif d > z:
                    break
        return ans


