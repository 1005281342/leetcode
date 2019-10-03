from typing import List

class Solution:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None

    def f(self, num):
        if self.a is None or self.b is None or self.c is None:
            return 0
        return num**2*self.a + num*self.b + self.c

    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        self.a = a
        self.b = b
        self.c = c
        return sorted([self.f(num) for num in nums])
