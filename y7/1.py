class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        d = dict()
        for i, v in enumerate(keyboard):
            d[v] = i

        res = 0
        p = 0
        for c in word:
            res += d[c] - p
            p = d[c]

        return res
