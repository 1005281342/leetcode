from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        cnt = 0
        for num in nums:
            if not len(str(num)) % 2:
                cnt += 1
        return cnt