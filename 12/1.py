from collections import defaultdict

class Leaderboard:

    def __init__(self):
        self.dd = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.dd[playerId] += score

    def reset(self, playerId: int) -> None:
        self.dd[playerId] = 0

    def top(self, K: int) -> int:
        t = sorted(self.dd.values(), reverse=True)[:K]
        return sum(t)

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
