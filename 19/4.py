from typing import List
from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:

        if len(arr) <= 0:
            return 0

        dd = defaultdict(set)
        for i, a in enumerate(arr):
            dd[a].add(i)
        print(dd)

        vit = len(arr) * [False]

        t = (arr[0], 0, 1)

        dq = deque()
        dq.append(t)
        while dq:
            v, i, cnt = dq.popleft()
            print(v, i, cnt)
            if vit[i]:
                continue
            vit[i] = True
            ii = max(dd[v])
            if len(dd[v]) > 1 and i != ii:
                if len(arr) - 1 in dd[v]:
                    return cnt

                dq.append((arr[ii], ii, cnt + 1))
            else:
                if 0 <= i - 1:
                    dq.append((arr[i - 1], i - 1, cnt + 1))
                if i + 1 < len(arr):
                    if i + 1 == len(arr) - 1:
                        return cnt
                    dq.append((arr[i + 1], i + 1, cnt + 1))
        # print(cnt)
        return cnt


if __name__ == '__main__':
    S = Solution()
    # S.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404])
    a = S.minJumps([11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13])
    print(a)
    # S.minJumps([6,1,9])
    # a = S.minJumps([7,6,9,6,9,6,9,7])
    # print(a)
