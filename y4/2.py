class Solution:
    def removeVowels(self, S: str) -> str:

        x = "aeiou"
        for c in x:

            S = S.replace(c, "")

        return S