from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

        return list(sorted(list(set(arr1) & set(arr2) & set(arr3))))