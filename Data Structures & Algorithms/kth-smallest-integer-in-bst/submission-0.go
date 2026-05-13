/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func kthSmallest(root *TreeNode, k int) int {
    var outVal int
	var dfs func(*TreeNode)

	dfs = func(root *TreeNode) {
		if root == nil || k == 0 {
			return
		}

		dfs(root.Left)
		k--
		if k == 0 {
			outVal = root.Val
			return
		}

		dfs(root.Right)
	}

	dfs(root)
	return outVal
}
