from typing import List
from collections import defaultdict, deque


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dd = defaultdict(set)
        for k, v, w in edges:
            if w > distanceThreshold:
                continue
            dd[k].add((v, w))
            dd[v].add((k, w))

        dd2 = defaultdict(set)
        for k, v, w in edges:
            if w > distanceThreshold:
                continue
            dd2[k].add(v)
            dd2[v].add(k)
        print(dd)
        print(dd2)
        # dw = defaultdict(set)
        # for k, v, w in edges:
        #     dw[w].add((k, v))
        #     dw[w].add((v, k))

        for k, v in dd.items():
            dq = deque()
            for c, w in v:
                if w >= distanceThreshold:
                    continue
                dq.append((c, w))
            while dq:
                c, w = dq.popleft()
                # if c == 0:
                #     print(c, w)
                print(dd[c])
                tmp = set()
                for ci, _ in dd[c]:
                    if c == 0:
                        print(ci)
                    for cvi, wi in dd[ci]:
                        if cvi in dd2[c] or cvi == c or cvi == ci:
                            continue
                        if wi + w > distanceThreshold:
                            continue

                        tmp.add((cvi, wi + w))
                        # dd[c].add((ci, wi + w))
                        # dd2[c].add(ci)
                for cc, ww in tmp:
                    dd[c].add((cc, ww))
                    dd2[c].add(cc)
        print(dd)
        print(dd2)
        tl = list()
        length = n + 1
        for k, vv in dd.items():
            v = [x for _, x in vv if x <= distanceThreshold]
            if len(v) < length:
                tl = [k]
                length = len(v)
            elif len(v) == length:
                tl.append(k)
        return max(tl)


if __name__ == '__main__':
    S = Solution()
    ans = S.findTheCity(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4)
    print(ans)
