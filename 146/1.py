class Solution:

    def count_num(self, num):

        return sum(range(1, num))

    def numEquivDominoPairs(self, dominoes: list) -> int:
        tt = list()
        td = dict()
        for d in dominoes:

            d = sorted(d)
            if d not in tt:
                tt.append(d)
                key = len(tt) - 1
                td[key] = 1
            else:
                key = tt.index(d)
                td[key] += 1

        return sum([self.count_num(num) for num in td.values() if num > 1])


S = Solution()
res = S.numEquivDominoPairs([[1, 2], [2, 1], [1, 2], [2, 1],[1, 2], [2, 1], [3, 4], [5, 6]])
print(res)
