from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.merge(nums, reverse=True)
        return heapq.nlargest(k, nums)
