from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        if numCourses == 1:
            return [0]

        dd = defaultdict(set)
        for a, b in prerequisites:
            dd[a].add(b)

        for i in range(numCourses):
            pass