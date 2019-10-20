from typing import List
from collections import defaultdict


class Solution:

    def removeSubfoldersX(self, folder: List[str]) -> List[str]:
        folder.sort()
        ki = tuple(folder[0].split('/'))
        dd = defaultdict(list)
        dd[ki].append(ki)
        for v in folder[1:]:
            vi = tuple(v.split('/'))
            if vi[:len(ki)] == dd[ki][0]:
                dd[ki].append(vi)
            else:
                dd[vi].append(vi)
                ki = vi
        print(dd)
        res = list()
        for v in dd.values():
            res.append("/".join(v[0]))
        # print(res)
        return res

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # for i in range(1):
        folder = self.removeSubfoldersX(folder)
        return folder


    # def removeSubfolders(self, folder: List[str]) -> List[str]:
    #     folder.sort()
    #     # print(folder)
    #     dd = defaultdict(list)
    #     k = "/" + folder[0].split("/")[1]
    #     dd[k].append(folder[0])
    #     for v in folder[1:]:
    #         tk = "/" + v.split("/")[1]
    #         if k == tk:
    #             dd[k].append(v)
    #             continue
    #         k = tk
    #         dd[k].append(v)
    #     print(dd)
