# class Solution:
#     def countOrders(self, n: int) -> int:
#         if n == 1:
#             return 1
#         return (self.countOrders(n - 1) * n * (2 * n - 1)) % (10 ** 9 + 7)


# import datetime
#
#
# class Solution:
#     def daysBetweenDates(self, date1: str, date2: str) -> int:
#         a,b,c = [int(i) for i in date1.split("-")]
#         d1 = datetime.datetime(a,b,c)  # 第一个日期
#         a, b, c = [int(i) for i in date1.split("-")]
#         d2 = datetime.datetime(a,b,c)  # 第二个日期
#         interval = d2 - d1  # 两日期差距
#         return interval.days  # 具体的天数

# from typing import List
#
#
# class Solution:
#
#     def check(self, digits):
#         s = "".join([str(i) for i in digits if i is not None])
#         if len(s) > 1 and s[0] == "0":
#             return "0"
#         return s
#
#     def largestMultipleOfThree(self, digits: List[int]) -> str:
#         digits.sort(reverse=True)
#         sd = sum(digits)
#         d = sd % 3
#         if d == 0:
#             return self.check(digits)
#         if sd < 3:
#             return ""
#
#         tmp = [i % 3 for i in digits]
#         # print(tmp)
#
#         for i in range(1, len(digits) + 1):
#             if d == tmp[-i]:
#                 digits[-i] = None
#                 return self.check(digits)
#
#         # print(tmp)
#
#         for i in range(1, len(digits)):
#             for j in range(i, len(digits) + 1):
#                 if tmp[-i] + tmp[-j] == d:
#                     digits[-i] = None
#                     digits[-j] = None
#                     return self.check(digits)
#         # print(tmp)
#         if tmp.count(1) < 3:
#             return self.check([digits[i] for i, v in enumerate(tmp) if v == 0])
#
#         for i in range(1, len(digits) - 1):
#             for j in range(i, len(digits)):
#                 for k in range(j, len(digits) + 1):
#                     if (tmp[-i] + tmp[-j] + tmp[-k]) % 3 == d:
#                         digits[-i] = None
#                         digits[-j] = None
#                         digits[-k] = None
#                         return self.check(digits)
#
#         return self.check([digits[i] for i in tmp if tmp == 0])
