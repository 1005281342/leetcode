class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        nums = [0] * 26
        i = 0
        while i < len(s):
            nums[ord(s[i]) - ord('a')] += 1
            nums[ord(t[i]) - ord('a')] += 1
            i += 1

        nums[ord(t[-1]) - ord('a')] += 1
        for i, num in enumerate(nums):
            if num:
                return chr(ord('a') + i)
