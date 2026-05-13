/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 
func deleteNode(root *TreeNode, key int) *TreeNode {
    if root == nil {
		return nil
	}

	if key > root.Val {
		root.Right = deleteNode(root.Right, key)
	} else if key < root.Val {
		root.Left = deleteNode(root.Left, key)
	} else {
		if root.Right == nil && root.Left == nil {
			return nil
		} else if root.Right == nil {
			return root.Left
		} else if root.Left == nil {
			return root.Right
		} else {
			minNode := findMin(root.Right)
			root.Val = minNode.Val
			root.Right = deleteNode(root.Right, minNode.Val)
			return root
		}
	}
	return root
}

func findMin(root *TreeNode) *TreeNode {
	targetTree := root
	for targetTree != nil && targetTree.Left != nil {
		targetTree = targetTree.Left
	}
	return targetTree
}

