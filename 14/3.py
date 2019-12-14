from typing import List
from collections import Counter


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        oc = Counter(parent)
        cur = 0
        while cur < nodes:
            st = value[cur] + sum(value[cur+1: cur+oc[parent[cur]+1]+1])
            print(st)
            cur += 1


if __name__ == '__main__':
    S = Solution()
    S.deleteTreeNodes(nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1])