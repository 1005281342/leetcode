from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        for a in arr:
            if a == 0 and arr.count(0) >= 2:
                return True

            if 2 * a in arr and a != 0:
                return True
        return False
