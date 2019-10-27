from typing import List
from collections import deque


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:

        ans = [start]
        at = [int(bin(start)[2:])]
        dq = deque((i for i in range(2 ** n)))
        while len(dq) > 1:
            i = dq.popleft()
            if i not in ans:
                t = int(bin(i)[2:])
                if str(at[-1] ^ t).count('1') == 1:
                    at.append(t)
                    ans.append(i)
                else:
                    dq.append(i)
        ans.append(dq[0])
        return ans


if __name__ == '__main__':

    S = Solution()
    r = S.circularPermutation(4, 1)
    print(r)