class Solution:
    def dieSimulator(self, n: int, rollMax: list) -> int:
        dp = [[0] * 16 for _ in range(7)]
        rollMax = [0] + rollMax
        limit = 10 ** 9 + 7
        for i in range(6):
            dp[i + 1][1] = 1
        for it in range(2, n + 1):
            ndp = [[0] * 16 for _ in range(7)]
            for i in range(0, 6 + 1):
                for j in range(1, 15 + 1):
                    if dp[i][j] == 0:
                        continue
                    for k in range(1, 6 + 1):
                        if i == k:
                            if j == rollMax[k]:
                                continue
                            ndp[k][j + 1] += dp[i][j]
                        else:
                            ndp[k][1] += dp[i][j]
            dp = ndp
            for i in range(7):
                for j in range(16):
                    dp[i][j] = int(dp[i][j])
                    dp[i][j] %= limit
        ans = sum([sum(a) for a in dp])
        return int(ans % limit)
