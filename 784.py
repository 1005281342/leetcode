from typing import List
from collections import deque


class Solution:

    def letterCasePermutation(self, S: str) -> List[str]:

        dq = deque()
        dq.append((list(S), 0))
        ans = list()
        while dq:
            t, c = dq.popleft()
            if c >= len(S) - 1:
                ans.append(''.join(t))
            while c < len(S):
                if t[c].isalpha():
                    dq.append((t[:], c + 1))

                    t[c] = chr(ord(t[c]) ^ 32)
                    dq.append((t, c + 1))
                    break
                c += 1

        return ans

    def letterCasePermutation2(self, S: str) -> List[str]:

        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [old + new for old in res for new in [ch, chr(ord(ch) ^ 32)]]
            else:
                res = [old + ch for old in res]
        return res


if __name__ == '__main__':
    S = Solution()
    # x = "3z4"
    x = "ccbba1b2"
    res = S.letterCasePermutation(x)
    res2 = S.letterCasePermutation2(x)
    print(res)
    print(res2)
    print(set(res) == set(res2))
