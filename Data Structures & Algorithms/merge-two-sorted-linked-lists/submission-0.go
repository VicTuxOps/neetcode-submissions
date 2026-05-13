/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    dummy := &ListNode{}
    out := dummy
    firstList := list1
    secondList := list2

    if firstList == nil {
        out = secondList
        return out
    } else if secondList == nil {
        out = firstList
        return out
    }

    for firstList != nil && secondList != nil {
        if firstList.Val <= secondList.Val {
            out.Next = firstList
            firstList = firstList.Next
            out = out.Next
        } else {
            out.Next = secondList
            secondList = secondList.Next
            out = out.Next
        }
        if firstList == nil {
            out.Next = secondList
        } else if secondList == nil {
            out.Next = firstList
        }
    }

    return dummy.Next
}
