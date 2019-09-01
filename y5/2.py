class Solution:
    def isArmstrong(self, N: int) -> bool:
        x = list(str(N))
        length = len(x)
        n = sum([int(i)**length for i in x])
        return N == n