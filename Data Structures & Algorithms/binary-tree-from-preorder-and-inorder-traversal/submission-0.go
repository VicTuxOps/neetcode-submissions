/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func buildTree(preorder []int, inorder []int) *TreeNode {
	//var newTree *TreeNode
	var dfs func(int, int) *TreeNode
	var idx int = 0

	if len(preorder) == 0 {
		return nil
	}
	//if len(preorder) == 1 {
	//	newTree = &TreeNode{Val: preorder[0]}
	//	return newTree
	//}

	inOderMap := make(map[int]int)
	for i, v := range inorder {
		inOderMap[v] = i
	}

	dfs = func(left, right int) *TreeNode {
		if left > right {
			return nil
		}

		nodeVal := preorder[idx]
		idx++
		newTree := &TreeNode{Val: nodeVal}
		mid := inOderMap[nodeVal]
		newTree.Left = dfs(left, mid - 1)
		newTree.Right = dfs(mid + 1, right)
		return newTree
	}
	return dfs(0, len(inorder)-1)
}
