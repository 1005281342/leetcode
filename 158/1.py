class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if not s:
            return 0

        stk = [s[0]]
        cnt = 0
        for c in s[1:]:
            if c != stk[-1]:
                stk.pop()
            else:
                stk.append(c)
            if not stk:
                cnt += 1
        return cnt