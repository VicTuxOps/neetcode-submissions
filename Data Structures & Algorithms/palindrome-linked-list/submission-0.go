/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func isPalindrome(head *ListNode) bool {
	i := 0
	j := 0
	dictPal := make(map[int]int)
	for head != nil {
		dictPal[i] = head.Val
		fmt.Println(head.Val)
		i++
		head = head.Next
	}
	
	i = i - 1
	for j < i {
		fmt.Println(j)
		fmt.Println(i)
		if dictPal[j] != dictPal[i] {
			return false
		}
		j++
		i--
	}
	return true
}