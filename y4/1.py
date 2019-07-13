class Solution:

    def isRunNian(self, Y: int):

        if not Y % 100:
            return not Y % 400

        return not Y % 4

    def numberOfDays(self, Y: int, M: int) -> int:
        run_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # 28, 29, 30, 31
        if self.isRunNian(Y) and M == 2:
            return run_list[M-1] + 1

        return run_list[M-1]


S = Solution()

print(S.numberOfDays(1900, 2))