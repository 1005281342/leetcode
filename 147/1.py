class Solution:
    def tribonacci(self, n: int) -> int:
        n_l = [0, 1, 1]
        if n <= 2:
            return n_l[n]
        else:
            for x in range(3, n + 1):
                n_l.append(sum(n_l[x - 3:x]))
        return n_l[-1]


if __name__ == '__main__':
    S = Solution()
    s = S.tribonacci(25)
    print(s)
