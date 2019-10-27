from typing import List
from collections import deque

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [i for i in arr if len(i) <= 26 and len(i) == len(set(i))]
        arr.sort(reverse=True)
        if not arr:
            return 0

        ans_lst = [0]
        dq = deque()
        ts = set()
        dq.append((arr[0]))
        ts.add(arr[0])
        while dq:
            v = dq.popleft()
            for i, vc in enumerate(arr):
                if len(v+vc) == len(set(v+vc)):
                    v += vc
                elif vc not in ts:
                    dq.append(vc)
                    ts.add(vc)
            ans_lst.append(len(v))

        return max(ans_lst)