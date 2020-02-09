class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = minutes * 6
        h = (hour % 12) * 30 + minutes / 2
        t = abs(m - h)
        return min(t, 360 - t)


if __name__ == '__main__':
    S = Solution()
    a = S.angleClock(12, 30)
    a = S.angleClock(4, 50)
    a = S.angleClock(12, 0)
    print(a)