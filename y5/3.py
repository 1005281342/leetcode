from typing import List


class Solution:
    def minimumCost(self, N: int, conections: List[List[int]]) -> int:

        conn = sorted(conections, key=lambda item: item[2])
        visited = []
        res = 0
        father = [i for i in range(N + 1)]
        for item in conn:
            i, j = item[0], item[1]
            cost = item[2]
            fi, fj = self.find(i, father), self.find(j, father)
            if fi == fj:
                continue
            res += cost
            father[fi] = fj
            visited.append((i, j))
        return res if len(visited) == N - 1 else -1

    def find(self, i, father):
        if father[i] == i:
            return i
        else:
            father[i] = self.find(father[i])
            return father[i]
