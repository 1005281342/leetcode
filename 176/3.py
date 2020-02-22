from typing import List
import heapq


class Solution:

    def maxEvents(self, events: List[List[int]]) -> int:
        lst = list()
        heapq.heapify(lst)
        events.sort()
        ms = dict()
        cnt = 0
        s = set()
        for a, b in events:
            if a == b and a not in s:
                s.add(a)
                ms[a] = True
                cnt += 1
                continue
            heapq.heappush(lst, (b, b - a, (a, b)))
        # print(lst)
        ti = 10005
        td = 0
        while lst:
            _, d, v = heapq.heappop(lst)
            a, b = v
            if td != d:
                ti = 10005
                td = d
            ti = min(ti, a)
            # print(ti)
            # for i in range(ti, b + 1):
            for i in range(b, ti-1, -1):
                if ms.get(i) is None and i not in s:
                    print(i)
                    cnt += 1
                    ms[i] = True
                    ti = i
                    break
        # print(ms)
        return min(cnt, len(events))


if __name__ == '__main__':
    S = Solution()
    S.maxEvents([[26,27],[24,26],[1,4],[1,2],[3,6],[2,6],[9,13],[6,6],[25,27],[22,25],[20,24],[8,8],[27,27],[30,32]])
