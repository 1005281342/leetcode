M = 1000000007


class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        if not arrLen:
            return 0

        if steps == 1:
            return 1

        sz = min(arrLen, steps)
        f = [0] * (sz + 10)
        cnt = 0
        for i in range(1, steps):
            g = [0] * (sz + 10)
            for j in range(sz):
                cnt += 1
                g[j] = (g[j] + f[j]) % M
                if j - 1 >= 0:
                    g[j] = (g[j] + f[j - 1]) % M
                if j + 1 < sz:
                    g[j] = (g[j] + f[j + 1]) % M
                f = g
        return f[0]
