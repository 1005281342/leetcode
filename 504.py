class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        flag = True
        if num < 0:
            num = - num
            flag = False
        stk = list()
        while num:
            stk.append(num % 7)
            num //= 7
        res = "".join([str(i) for i in stk[::-1]])
        return res if flag else "-"+res
