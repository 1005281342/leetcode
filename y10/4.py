from collections import Counter


class Solution:

    def isValidPalindrome(self, s: str, k: int) -> bool:

        return self.is_kpal(s, k)

    def is_kpal_r(self, str1, str2, m, n):

        if not m:
            return n

        if not n:
            return m

        if str1[m - 1] == str2[n - 1]:
            return self.is_kpal_r(str1, str2, m - 1, n - 1)

        res = 1 + min(self.is_kpal_r(str1, str2, m - 1, n),
                      (self.is_kpal_r(str1, str2, m, n - 1)))

        return res

    def is_kpal(self, string, k):
        rs = string[::-1]
        l = len(string)

        return self.is_kpal_r(string, rs, l, l) <= k * 2
