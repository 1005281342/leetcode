class Solution:

    def __init__(self):
        self.cnt = 0

    def h(self, n, m):

        if n < m:
            n, m = m, n

        if m == 1:
            self.cnt += n
            return

        self.cnt += 1
        if m == n:
            return
        return self.h(m, n - m)

    def tilingRectangle(self, n: int, m: int) -> int:

        self.h(n, m)
        return self.cnt