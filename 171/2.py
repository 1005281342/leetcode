class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        sa = bin(a)[2:]
        sb = bin(b)[2:]
        sc = bin(c)[2:]
        ans = 0
        if len(sc) < len(sa):
            for i in sa[:len(sa) - len(sc)]:
                if i == "1":
                    ans += 1
            sa = sa[len(sa) - len(sc):]
        if len(sa) < len(sc):
            sa = "0" * (len(sc) - len(sa)) + sa

        if len(sc) < len(sb):
            for i in sb[:len(sb) - len(sc)]:
                if i == "1":
                    ans += 1
            sb = sb[len(sb) - len(sc):]
        if len(sb) < len(sc):
            sb = "0" * (len(sc) - len(sb)) + sb

        for i in range(len(sc)):
            if sc[i] == "1":
                if sa[i] == "1" or sb[i] == "1":
                    continue
                else:
                    ans += 1
            else:
                if sa[i] == "1":
                    ans += 1
                if sb[i] == "1":
                    ans += 1
        return ans


if __name__ == '__main__':
    S = Solution()
    S.minFlips(6, 9, 2)
