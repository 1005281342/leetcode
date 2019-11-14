from typing import List
from collections import defaultdict


class Solution:

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for s in strings:
            if len(s) == 1:
                dd["1"].append(s)
                continue
            t = "0"
            for j in s[1:]:
                tt = ord(j)-ord(s[0])
                if 0<= tt:
                    t += str(chr(tt))
                else:
                    t += str(chr(26+tt))
            dd[t].append(s)
        # print(dd)
        return [list(sorted(dd[k])) for k in sorted(dd.keys())]