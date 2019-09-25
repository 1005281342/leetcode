from typing import List
from collections import Counter


class Solution:
    def robot(self, command: str, ob: List[List[int]], sx: int, sy: int) -> bool:
        dc = Counter(command)
        n = dc['R']
        m = dc['U']
        x, y = 0, 0
        vo = vs = False
        for ch in command:
            if ch == 'R':
                x += 1
            else:
                y += 1
            if (x, y) == (sx, sy):
                return True
            if (sx - x) % n == 0 and (sy - y) % m == 0 and (sx - x) // n == (sy - y) // m:
                vs = True
            for ox, oy in ob:
                if (x, y) == (ox, oy):
                    return False
                if ox <= sx and oy <= sy:
                    if (ox - x) % n == 0 and (oy - y) % m == 0 and (ox - x) // n == (oy - y) // m:
                        vo = True
        return (not vo) and vs
