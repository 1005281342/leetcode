from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        ans = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]

