from collections import Counter

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:

        if len(s1) != len(s2):
            return -1

        tc = Counter(s1+s2)
        if tc['x'] % 2 or tc['y'] % 2:
            return -1

        ts1 = list(s1)
        ts2 = list(s2)
        tql = list()
        for i in range(len(s1)):
            if ts1[i] != ts2[i]:
                tql.append((ts1[i]))

        tt = Counter(tql)
        l = len(tql)
        if l % 2:
            return -1
        txx = tt.get('x') or 0
        x, xq = txx // 2, txx % 2
        tyy = tt.get('y') or 0
        y, yq = tyy // 2, tyy % 2
        return x + y + xq + yq


if __name__ == '__main__':
    S = Solution()
    res = S.minimumSwap("xxyyxyxyxx",
                        "xyyxyxxxyx")
    print(res)

    """
        x x y y x y x y x x
                      x  
                  y
        x y y x y x x x y x
    """
