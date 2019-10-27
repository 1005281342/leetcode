class Solution(object):

    def get_ans(self, nums):
        ans = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        length = len(nums)
        if length <= 3:
            return ans[:length]

        return ans + [str(i) for i in range(4, length+1)]

    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        ans = self.get_ans(nums)
        t = sorted(nums, reverse=True)
        d = dict()
        for k, v in zip(t, ans):
            d[k] = v

        res = [d[i] for i in nums]
        return res