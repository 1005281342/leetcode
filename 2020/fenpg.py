from math import gcd, ceil

modt = 1000000007


def helper(a, b, m):
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % m
        a = a * a % m
        b >>= 1
    return ans


class Solution:
    def findNum(self, n: int, k: int) -> int:
        return int((n * helper(ceil(n / gcd(n, n - k)), n, modt)) - (n - k)) % modt


S = Solution()
ans = S.findNum(2, 1)
print(ans)

ans = S.findNum(3, 1)
print(ans)

ans = S.findNum(4, 2)
print(ans)
