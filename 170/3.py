from typing import List
from collections import defaultdict, Counter


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], uid: int, level: int):
        ddf = defaultdict(set)

        for i, v in enumerate(friends):
            for c in v:
                ddf[i].add(c)
                ddf[c].add(i)

        if level == 0:
            return sorted(watchedVideos[uid])

        ddl = defaultdict(set)
        t = 1
        # ddl[0].add(uid)
        ddl[0].add(0)
        s = set()
        while t <= len(watchedVideos):  # level
            for c in ddl[t - 1]:
                if c in s:
                    continue
                ddl[t] |= ddf[c]
                s.add(c)
            t += 1

        # aa = ddl[level]
        aa = ddl[uid+level]
        if ddl.get(uid-level):
            aa |= ddl.get(uid-level)
        x = list()
        for a in aa:
            if a != uid:
                x.extend(watchedVideos[a])

        cd = Counter(x)
        ddcd = defaultdict(list)
        for k, v in cd.items():
            ddcd[v].append(k)
        ans = list()
        for kc in sorted(ddcd.keys()):
            ans.extend(sorted(ddcd[kc]))
        return ans
