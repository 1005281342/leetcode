

# class Solution:
#     def connectSticks(self, sticks: List[int]) -> int:
#
#         sticks.sort()
#         res = 0
#         for i in range(len(sticks) - 1):
#             k = sticks[i] + sticks[i+1]
#             res += k
#
#             sticks[i+1] = k
#         return res

from typing import List
import heapq


class Solution:

    def connectSticks(self, sticks: List[int]) -> int:

        if len(sticks) <= 2:
            return sum(sticks)

        heapq.heapify(sticks)
        res = k = heapq.heappop(sticks) + heapq.heappop(sticks)

        while sticks:
            m = heapq.heappop(sticks)
            if sticks:
                n = heapq.heappop(sticks)
                if k > n:
                    heapq.heappush(sticks, k)
                    k = m + n
                else:
                    heapq.heappush(sticks, n)
                    k += m
                res += k
            else:
                k += m
                res += k
        return res

    # def __init__(self):
    #
    #     self.d = dict()

    # def Add(self, v):
    #
    #     if self.d.get(v):
    #         self.d[v] += 1
    #     else:
    #         self.d[v] = 1

    # todo timeout
    # def connectSticks(self, sticks: List[int]) -> int:
    #
    #     # for v in sticks:
    #     #     self.Add(v)
    #
    #     sticks.sort(reverse=True)
    #
    #     res = k = sticks.pop() + sticks.pop()
    #
    #     while sticks:
    #         m = sticks.pop()
    #         if sticks:
    #             n = sticks.pop()
    #             if k > n:
    #                 sticks.append(k)
    #                 sticks.sort(reverse=True)
    #                 k = m + n
    #             else:
    #                 sticks.append(n)
    #                 k += m
    #             res += k
    #         else:
    #             k += m
    #             res += k
    #
    #     return res


if __name__ == '__main__':
    S = Solution()
    res = S.connectSticks([2, 4, 3])
    print(res)
    res = S.connectSticks([3354, 4316, 3259, 4904, 4598, 474, 3166, 6322, 8080, 9009])
    print(res)
