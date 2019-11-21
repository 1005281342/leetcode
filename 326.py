# from math import log
#
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         t = log(n, 3)
#         return t == int(t)

res = {
    0: 1,
    1: 4,
}
for i in range(2, 17):
    res[i] = res[i - 1] * 4
# print(res)

d = dict()
for v, k in res.items():
    d[k] = v
print(d)
