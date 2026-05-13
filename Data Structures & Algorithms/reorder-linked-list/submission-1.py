# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow.next
        slow.next = None # Split the list
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        l1, l2 = head, prev
        while l2:
            # Save the next nodes
            temp1 = l1.next
            temp2 = l2.next
            
            # Re-wire the pointers
            l1.next = l2
            l2.next = temp1
            
            # Advance the pointers
            l1 = temp1
            l2 = temp2