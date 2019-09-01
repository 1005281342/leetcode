class Solution:

    def ordinalOfDate(self, date: str) -> int:
        Y, M, D = [int(i) for i in date.split('-')]
        return sum([self.numberOfDays(Y, M)[i] for i in range(0, M-1)]) + D

    def isRunNian(self, Y: int):

        if not Y % 100:
            return not Y % 400

        return not Y % 4

    def numberOfDays(self, Y: int, M: int) -> list:
        run_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # 28, 29, 30, 31
        if self.isRunNian(Y):
            run_list[M-1] += 1

        return run_list
