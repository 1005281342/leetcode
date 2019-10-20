from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        tmp = coordinates[0][0]
        cnt = 0
        cnty = 0
        tmpy = coordinates[0][1]
        for x, y in coordinates:
            if x == tmp:
                cnt += 1
            if y == tmpy:
                cnty += 1
        lc = len(coordinates)
        if lc == cnt or lc ==tmpy:
            return True
        k = (coordinates[-1][1] - coordinates[0][1]) / (coordinates[-1][0] - coordinates[0][0])
        for x, y in coordinates[1:]:
            try:
                if (y - coordinates[0][1]) / (x - coordinates[0][0]) != k:
                    return False
            except:
                return False
        return True
            