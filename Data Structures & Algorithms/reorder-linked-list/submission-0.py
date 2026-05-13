# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mynodes = {}
        i = 0
        track = head
        while track != None:
            mynodes[i] = track
            track = track.next
            i+=1
        
        left = 0
        right = i-1
        while left < right:
            print(left)
            mynodes[left].next = mynodes[right]
            left+=1
            if left == right:
                break
            else:
                mynodes[right].next = mynodes[left]
                right -=1
        
        mynodes[left].next = None