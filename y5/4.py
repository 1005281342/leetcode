from typing import List
import collections


class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        indegree = [0] * (N + 1)
        graph = collections.defaultdict(set)
        for item in relations:
            indegree[item[1]] += 1
            graph[item[0]].add(item[1])
        used = set()
        step = 1
        deq = collections.deque()
        for i in range(1, len(indegree)):
            if indegree[i] == 0:
                deq.append(i)
                used.add(i)
        if len(used) == N:
            return 1
        while deq:
            cnt = 0
            size = len(deq)
            step += 1
            while cnt < size:
                front = deq.popleft()
                for adj in graph[front]:
                    if adj not in used:
                        indegree[adj] -= 1
                        if indegree[adj] == 0:
                            deq.append(adj)
                            used.add(adj)
                cnt += 1
            if len(used) == N:
                return step
        return -1
