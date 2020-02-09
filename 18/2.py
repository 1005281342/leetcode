class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""

        t = list(palindrome)
        for i, v in enumerate(t):
            for c in range(97, 97 + 26):
                if chr(c) > v:
                    break
                t[i] = chr(c)
                if t != t[::-1]:
                    return "".join(t)
                t[i] = v

        for c in range(97, 97 + 26):
            t[-1] = chr(c)
            if t != t[::-1]:
                return "".join(t)
            t[-1] = v

        return ""
