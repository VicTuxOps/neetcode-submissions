/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeKLists(lists []*ListNode) *ListNode {
    k := len(lists)
	mergedList := &ListNode{}

	if k == 0 {
		return nil
	}
	if k == 1 {
		return lists[0]
	}

	head := mergedList
	kMiddle := k/2
	firstHalf := mergeKLists(lists[:kMiddle])
	secondHalf := mergeKLists(lists[kMiddle:])

	for firstHalf != nil && secondHalf != nil {
		if firstHalf.Val <= secondHalf.Val {
			head.Next = firstHalf
			head = head.Next
			firstHalf = firstHalf.Next
		} else {
			head.Next = secondHalf
			head = head.Next
			secondHalf = secondHalf.Next
		}
	}

	if firstHalf != nil {
		head.Next = firstHalf
	} else if secondHalf != nil {
		head.Next = secondHalf
	}

	return mergedList.Next
}
