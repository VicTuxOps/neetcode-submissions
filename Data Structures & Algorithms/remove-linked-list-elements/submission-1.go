/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func removeElements(head *ListNode, val int) *ListNode {
	tmp := head
	i := 0
	for tmp != nil {
		if tmp.Val == val && i == 0 {
			head = head.Next
			tmp = tmp.Next
			i--
		} else if tmp.Next != nil && tmp.Next.Val == val {
			tmp.Next = tmp.Next.Next
		} else {
			tmp = tmp.Next
		}
		i++
		
	}
	return head
}
