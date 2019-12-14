from typing import List


class Solution:

    def help(self, a, b):
        x = (4 * a - b) / 2
        if a != 0 and (4 * a - b) % (x * 2) == 0:
            y = a - x
            if int(x) != x or int(y) != y:
                return []
            return [int(y), int(x)]
        return []

    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if 4 * cheeseSlices < tomatoSlices:
            return list()
        if 2 * cheeseSlices > tomatoSlices:
            return list()
        if tomatoSlices % 2:
            return list()

        return self.help(cheeseSlices, tomatoSlices)
        # for i in range(cheeseSlices+1):
        #     if i*2 + (cheeseSlices-i) *4 == tomatoSlices:
        #         return [cheeseSlices-i, i]
