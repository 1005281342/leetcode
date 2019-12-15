# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        lst = list()
        while head:
            lst.append(head.val)
            head = head.next

        c = 0
        for i, v in enumerate(lst[::-1]):
            c += 2 ** i * v

        return c
