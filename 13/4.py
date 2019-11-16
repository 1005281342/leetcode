class Solution:
    def numberOfWays(self, num_people: int) -> int:
        if num_people == 2:
            return 1

        d = num_people >> 1
        # print(d)
        # (2n)! / [n!(n + 1)!]

        # o = list(range(2, num_people + 1, 2))
        # d = list(range(1, num_people, 2))
        # print(o, d)


if __name__ == '__main__':
    S = Solution()
    S.numberOfWays(8)
