from typing import List
# from collections import Counter
#
# class Solution:
#     def minSwaps(self, data: List[int]) -> int:
#
#         d = Counter(data)
#         L = d[1]
#         res = L
#         for i in range(len(data) - L):
#             # res.append(Counter(data[i:i+L])[0])
#             res = Counter(data[i:i+L])[0] if Counter(data[i:i+L])[0] < res else res
#         return res

class Solution:
    def minSwaps(self, data: List[int]) -> int:

        L = sum(data)
        res = L
        for i in range(len(data) - L):
            k = L - sum(data[i:i+L])
            res = k if k < res else res
        return res


if __name__ == '__main__':
    pass