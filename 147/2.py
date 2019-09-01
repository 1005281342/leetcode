class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        res = ""
        d = {'a': (0, 0), 'b': (0, 1), 'c': (0, 2), 'd': (0, 3), 'e': (0, 4), 'f': (1, 0), 'g': (1, 1), 'h': (1, 2),
             'i': (1, 3), 'j': (1, 4), 'k': (2, 0), 'l': (2, 1), 'm': (2, 2), 'n': (2, 3), 'o': (2, 4), 'p': (3, 0),
             'q': (3, 1), 'r': (3, 2), 's': (3, 3), 't': (3, 4), 'u': (4, 0), 'v': (4, 1), 'w': (4, 2), 'x': (4, 3),
             'y': (4, 4), 'z': (5, 0)}
        start = (0, 0)
        for ns in target:
            nxt = d[ns]
            UD = nxt[0] - start[0]
            if UD > 0:
                if start[1] > 0 and nxt[0] == 5:
                    res += "D" * (4 - start[0])
                    UD -= (4 - start[0])
                else:
                    res += "D" * UD
                    UD = 0
            else:
                res += "U" * (-UD)
            LR = nxt[1] - start[1]
            if LR > 0:
                res += "R" * LR
            else:
                res += "L" * (-LR)
            res += "D"*UD
            res += "!"
            start = nxt
        return res


if __name__ == '__main__':
    S = Solution()
    res = S.alphabetBoardPath("leet")
    print(res)
