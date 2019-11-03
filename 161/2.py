from typing import List
from collections import Counter
from itertools import combinations

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        tn = [num % 2 for num in nums]
        if Counter(tn)[1] < k:
            return 0

        tl = len(nums)

        tt = tn[:]
        for n in tn[1:]:
            tt[n] += tt[n-1]

        for i in range(k,)