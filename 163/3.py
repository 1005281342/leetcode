from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        ok = list()
        q = list()
        for num in nums:
            if num % 3:
                q.append(num)
            else:
                ok.append(num)

        a = 0
        b = len(q) - 1
        while a < b:
            t = q[a] + q[b]
            if t % 3 == 0:
                ok.append(t)
                a += 1
                b -= 1
            elif (q[a+1] + q[b]) % 3 == 0:
                ok.append(q[a+1] + q[b])
                a += 2
                b -= 1
            elif (q[a] + q[b-1]) % 3 == 0:
                ok.append(q[a] + q[b-1])
                a += 1
                b -= 2


