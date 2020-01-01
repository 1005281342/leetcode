from typing import List
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        dq = deque()
        dq.append(start)
        s = set()
        while dq:
            index, now = dq.pop()
            if arr[index] == 0:
                return True

            for d in [arr[index], -arr[index]]:
                d += index
                if 0 <= d < len(arr) and (index, d) not in s:
                    dq.append(d)
                    s.add((index, d))
        return False


"""
0 
3 -3

"""