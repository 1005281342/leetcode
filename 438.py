from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        res = list()
        if len(p) > len(s):
            return res

        ls = len(s)
        lp = len(p)
        cp = Counter(p)
        for i in range(ls - lp + 1):
            if Counter(s[i:i + lp]) == cp:
                res.append(i)
        return res
