from typing import List


class Solution:

    def max_length(self, s, k):
        p, q = 0, len(s)
        while p < q:
            if sum(s[p:q+1]) <= k:
                return q - p
            elif s[p] <= s[q]:
                q -= 1
            else:
                p += 1
        return 0

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        length = len(s)
        d = [0]*length
        for i in range(length):
            d[i] = abs(ord(s[i]) - ord(t[i]))

        # 求
        return self.max_length(d, maxCost)
