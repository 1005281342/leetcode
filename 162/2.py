from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []

        for num in colsum:
            if num > 2 or num < 0:
                return []

        a = [0] * len(colsum)
        b = [0] * len(colsum)

        c = upper
        d = lower

        for i, num in enumerate(colsum):
            if num == 0:
                continue
            if num == 2:
                a[i] += 1
                b[i] += 1
            if num == 1:
                if upper < 0 or lower < 0:
                    return []

                if upper >= lower:
                    a[i] += 1
                    upper -= 1
                else:
                    b[i] += 1
                    lower -= 1
        if sum(a) != c or sum(b)!= d:
            return []

        return [a, b]

