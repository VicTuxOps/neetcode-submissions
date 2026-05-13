/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func inorderTraversal(root *TreeNode) []int {
	outArr := []int{}
	if root == nil {
		return outArr
	}
	
	leftArr := inorderTraversal(root.Left)
	outArr = append(outArr, leftArr...)
	outArr = append(outArr, root.Val)
	rightArr := inorderTraversal(root.Right)
	outArr = append(outArr, rightArr...)
	return outArr
}
