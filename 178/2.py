from typing import List
from collections import Counter, defaultdict


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]

        # t = (0,) * len(votes[0])
        # print(t)
        cd = dict()
        for a in votes[0]:
            cd[a] = [0] * len(votes[0])

        for v in votes:
            for i, c in enumerate(v):
                cd[c][i] += 1

        td = defaultdict(list)
        for v, k in cd.items():
            td[tuple(k)].extend(v)
        # print(sorted(td.keys()))
        ans = list()
        for k in sorted(td.keys(), reverse=True):
            ans.extend(sorted(td[k]))

        return "".join(ans)

        # n = len(set("".join(votes)))
        # print(n, len(set(votes[0])))

        # d = defaultdict(int)
        # for k, v in cd.items():
        #     for i, c in enumerate(k):
        #         d[c] += (i + 1) * v
        # print(d)
        # dd = defaultdict(list)
        # for k, v in d.items():
        #     dd[v].append(k)
        # # print(dd)
        # ans = list()
        # for k in sorted(dd.keys()):
        #     ans.extend(list(sorted(dd[k])))
        # print(ans)
        # return "".join(ans)


if __name__ == '__main__':
    S = Solution()
    a = S.rankTeams(
        ["BCA","CAB","CBA","ABC","ACB","BAC"])
    print(a)