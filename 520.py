class Solution(object):
    def detectCapitalUse(self, word: str):
        """
        :type word: str
        :rtype: bool
        """
        head = word[0]
        if head.lower() == head:
            return word == word.lower()
        return word[1:] == word[1:].lower() or word[1:] == word[1:].upper()
