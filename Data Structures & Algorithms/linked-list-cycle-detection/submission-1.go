/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func hasCycle(head *ListNode) bool {
	cur := head
	tail := head
    for (tail != nil && tail.Next != nil) {
		cur = cur.Next
		tail = tail.Next.Next
		if cur == tail {
			return true
		}
	}
	return false
}
