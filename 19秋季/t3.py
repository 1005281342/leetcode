from typing import List


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:

        if len(cont) == 1:
            return [cont[0], 1]

        t = [[1, cont.pop()]]