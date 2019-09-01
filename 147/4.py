class Solution:
    def stoneGameII(self, piles: list) -> int:
        dp = {}

        def search(st, bigm):
            if (st, bigm) in dp:
                return dp[(st, bigm)]
            if len(piles) - st <= 2 * bigm:
                dp[st, bigm] = sum(piles[st:])
                return dp[(st, bigm)]
            tmp = 0
            for i in range(1, 2 * bigm + 1):
                cur = sum(piles[st:st + i])
                cur += sum(piles[st + i:]) - search(st + i, max(bigm, i))
                tmp = max(tmp, cur)
            dp[(st, bigm)] = tmp
            return tmp

        search(0, 1)
        return dp[0, 1]
