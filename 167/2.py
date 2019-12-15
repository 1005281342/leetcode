from typing import List

t = [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345,
     23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789,
     123456789]


class Solution:

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # ls = str(low)
        # k = 10 ** (len(ls) - 1)
        # c = low
        # res = list()
        # while c <= high + k:
        #     for b in range(c, c + k):
        #         flag = True
        #         b = str(b)
        #         tt = b[0]
        #         for i in b[1:]:
        #             if int(i) - int(tt) != 1:
        #                 flag = False
        #             tt = i
        #         if flag:
        #             res.append(int(b))
        #             break
        #     c += k

        return [i for i in t if low <= i <= high]
