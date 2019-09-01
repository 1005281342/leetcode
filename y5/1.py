class Solution:
    def largestUniqueNumber(self, A: list) -> int:

        d = {}
        for a in A:
            if d.get(a):
                d[a] += 1
            else:
                d[a] = 1

        s = [k for k, v in d.items() if v == 1] or [-1]
        return sorted(s)[-1]
