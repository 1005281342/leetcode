MAX = 2147483647
from itertools import permutations


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n >= MAX or n < 10:
            return -1

        t = list(str(n))
        if t == sorted(t, reverse=True):
            return -1
        # t[-1], t[-2] = t[-2], t[-1]
        if t[-1] > t[-2]:
            t[-1], t[-2] = t[-2], t[-1]
            return int("".join(t))

        s = [t[-1], ]
        for k in range(1, len(t)):
            s.append(t[-k - 1])
            if t[-k] > t[-k - 1]:
                break
        tar = int("".join(t[-k-1:]))
        tmp = [tar, ]
        for c in permutations(s):
            tt = int("".join(c))
            # print(tt, tar)
            if tt > tar:
                tmp.append(tt)
        # print(tmp)
        res = int("".join(t[:-k-1]) + str(sorted(tmp)[1]))
        return res if res <= MAX else -1


if __name__ == '__main__':
    S = Solution()
    res= S.nextGreaterElement(1999999999)
    print(res)
