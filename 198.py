class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [0, ]
        b = [0, ]
        for i, num in enumerate(nums):
            if i % 2:
                a.append(num)
            else:
                b.append(num)
        return max(sum(a), sum(b))
