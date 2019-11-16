from typing import List
from collections import defaultdict, deque


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        dd = defaultdict(set)
        ws = text.split(" ")
        h = set()
        res = {text, }
        for a, b in synonyms:
            dd[a].add(b)
            dd[b].add(a)
        wd = set(ws) & set(dd.keys())
        dq = deque(((w, text) for w in wd))
        cnt = len(wd) * 1000
        while dq and cnt:
            v, ww = dq.popleft()
            # if v not in h:
            #     h.add(v)
            dq.extend((kv, ww.replace(v, kv)) for kv in dd[v])
            for w in wd:
                if w == v:
                    continue
                for c in dd[w]:
                    t = ww.replace(w, c)
                    if t not in res:
                        dq.append((c, t))
                    res.add(t)
                    cnt -= 1
        return sorted(list(res))

if __name__ == '__main__':
    S = Solution()
    x = S.generateSentences([["a","b"],["c","d"],["e","f"]],
"a c e")
    print(x)
    print(len(x))