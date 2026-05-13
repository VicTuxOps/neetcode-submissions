/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type ListNode struct {
	Val  *TreeNode
	Next *ListNode
}

type Queue struct {
	Left  *ListNode // front of Queue
	Right *ListNode // back of Queue
	Size  int
}

func NewQueue() *Queue {
	return &Queue{
		Left:  nil,
		Right: nil,
	}
}

func NewListNode(val *TreeNode) *ListNode {
	return &ListNode{
		Val:  val,
		Next: nil,
	}
}

func (q *Queue) Enqueue(val *TreeNode) {
	newNode := NewListNode(val)
	if q.Right != nil {
		// Queue is not empty
		q.Right.Next = newNode
		q.Right = q.Right.Next
	} else {
		// Queue is empty
		q.Left = newNode
		q.Right = newNode
	}
	q.Size++
}

func (q *Queue) Dequeue() *TreeNode {
	if q.Left == nil {
		// Queue is empty
		os.Exit(0)
	}
	val := q.Left
	q.Left = q.Left.Next
	if q.Left == nil {
		q.Right = nil
	}
	q.Size--
	return val.Val
}

func levelOrder(root *TreeNode) [][]int {
    if root == nil {
		return nil
	}

	var subList [][]int
	queue := NewQueue()
	queue.Enqueue(root)

	for queue.Size > 0 {
		level := make([]int, 0)
		levelSize := queue.Size
		for i := 0; i < levelSize; i++ {
			curr := queue.Dequeue()
			level = append(level, curr.Val)
			if curr.Left != nil {
				queue.Enqueue(curr.Left)
			}
			if curr.Right != nil {
				queue.Enqueue(curr.Right)
			}
		}
		subList = append(subList, level)
	}
	return subList
}
