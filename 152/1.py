class Solution:

    def numPrimeArrangements(self, n: int) -> int:
        zs_lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        dd = (10 ** 9 + 7)

        d = dict()
        for k, v in enumerate(zs_lst):
            d[v] = k + 1
        cn = n
        while True:
            if cn in zs_lst:
                e = d[cn]
                break
            else:
                cn -= 1
        # print(e)
        a = 1
        for i in range(1, e + 1):
            a *= i

        b = 1
        for i in range(1, n - e + 1):
            b *= i
            b %= dd
        # print(a% (10 ** 9 + 7)*(b% (10 ** 9 + 7)))
        return (a * b) % dd


if __name__ == '__main__':

    S = Solution()
    print(S.numPrimeArrangements(100))