# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, dummy
        for i in range(n):
            if right is None:
                break
            right = right.next
        track = head
        while right.next:
            left = left.next
            right = right.next
        if left.next is not None:
            left.next = left.next.next
        else:
            track = None
        return dummy.next