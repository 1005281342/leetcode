# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#
#         if len(num) <= k:
#             return "0"
#
#         tmp = list(num)
#         cnt = 0
#         while (cnt < len(num) - 1) and k:
#             if tmp[cnt] < tmp[cnt+1]:
#                 k -= 1
#             cnt += 1
#         x = "".join(tmp)
#         if len(x) <= k:
#             return "0"
#         x = x[:len(x)-k]
#         if not x:
#             return "0"
#         return str(int(x))