from typing import List

class Solution:

    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(B))] for _ in range(len(A))]
        la = len(A[0])
        for i in range(len(A)):

            for j in range(len(B)):

                for k in range(la):
                    res[i][j] += A[i][k]*B[k][j]
        return res
