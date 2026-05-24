# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #sum both lists
        l3 = ListNode()
        res = l3
        carry = 0
        while l1 and l2:
            tmp = l1.val + l2.val + carry
            if tmp > 9:
                carry = tmp // 10
                tmp = tmp % 10
            else:
                carry = 0
            
            l3.next = ListNode(tmp)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
            tmp = 0
        
        while l1:
            tmp = l1.val + carry
            if tmp > 9:
                carry = tmp // 10
                tmp = tmp % 10
            else:
                carry = 0
            l3.next = ListNode(tmp)
            l3 = l3.next
            l1 = l1.next
            tmp = 0
        
        while l2:
            tmp = l2.val + carry
            if tmp > 9:
                carry = tmp // 10
                tmp = tmp % 10
            else:
                carry = 0
            l3.next = ListNode(tmp)
            l3 = l3.next
            l2 = l2.next

        print(carry)
        if carry > 0:
            l3.next = ListNode(carry)

        return res.next
