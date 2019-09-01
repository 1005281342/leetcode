from typing import List


class Solution:

    def Add(self, time, name, city, transaction, dd):

        if dd.get((time, name, city)):
            dd[(time, name, city)].append(transaction)
        else:
            dd[(time, name, city)] = [transaction]

        return dd

    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        res = []
        dd = dict()  # 按时间
        for transaction in transactions:

            name, time, amount, city = transaction.split(',')
            time = int(time)
            amount = int(amount)

            # N
            if amount > 1000:
                res.append(transaction)

            flag = False
            for tt in dd.keys():
                t, n, c = tt
                if abs(t - time) <= 60 and n == name and c!=city:
                    flag = True
                    res.extend(dd[tt])
            if flag:
                res.append(transaction)

            dd = self.Add(time, name, city, transaction, dd)
        # print(dd)
        # print(list(set(res)))
        return list(set(res))


if __name__ == '__main__':

    S = Solution()
    S.invalidTransactions(["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"])