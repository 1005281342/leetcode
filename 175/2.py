from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if s == t:
            return 0

        cs = Counter(s)
        ct = Counter(t)
        # print(cs, ct)
        if cs == ct:
            return 0

        t1 = 0
        t2 = 0
        for k, v in cs.items():
            if ct.get(k):
                t1 += abs(v - ct.get(k))
            else:
                t2 += v
        # print(t1, t2)
        if t1 % 2:
            k1 = t1 // 2 + 1 + t2
        else:
            k1 = t1 // 2 + t2

        t1 = 0
        t2 = 0
        for k, v in ct.items():
            if cs.get(k):
                t1 += abs(v - cs.get(k))
            else:
                t2 += v
        # print(t1, t2)
        if t1 % 2:
            kk = t1 // 2 + 1 + t2
        else:
            kk = t1 // 2 + t2
        # print(k1, kk)
        return (k1 + kk)//2


if __name__ == '__main__':
    S = Solution()
    S.minSteps(s="friend", t="family")
    S.minSteps(s="leetcode", t="practice")
    S.minSteps(s="bab", t="aba")
    S.minSteps(s="anagram", t="mangaar")
    S.minSteps("gctcxyuluxjuxnsvmomavutrrfb",
"qijrjrhqqjxjtprybrzpyfyqtzf")
