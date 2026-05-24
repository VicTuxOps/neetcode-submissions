# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #l1 number
        l1num = ""
        while l1:
            l1num = str(l1.val) + l1num
            l1 = l1.next

        #l2 number
        l2num = ""
        while l2:
            l2num = str(l2.val) + l2num
            l2 = l2.next

        l3num = str(int(l1num) + int(l2num))
        l3 = ListNode()
        res = l3
        for i in range(len(l3num)-1, -1, -1):
            tmp = ListNode(int(l3num[i]))
            l3.next = tmp
            l3 = l3.next

        return res.next
