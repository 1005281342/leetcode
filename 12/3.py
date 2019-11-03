from typing import List
from collections import Counter, defaultdict, deque

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        dd = defaultdict(list)
        for a, b in edges:
            dd[a].append(b)
            dd[b].append(a)

        t = list()
        for edge in edges:
            t.extend(edge)

        ct = Counter(t)
        res = ct.most_common(1)
        dq = deque([(a, 0) for a, _ in res])
        xd = defaultdict(list)
        xs = set()
        while dq:
            x, d = dq.popleft()
            xd[x].append(d)
            for v in dd[x]:
                if (x, v) not in xs or (v, x) not in xs:
                    dq.append((v, d + 1))
                    xs.add((x, v))
                    xs.add((v, x))
        ans = 0
        for v in xd.values():
            print(v)
            x = sum(sorted(v, reverse=True)[:2])
            if x > ans:
                ans = x
        print(ans)
        return ans + 1





if __name__ == '__main__':

    S = Solution()
    S.treeDiameter([[0,1],[1,2],[2,3],[2,4],[0,5],[1,6],[2,7],[6,8],[8,9]])