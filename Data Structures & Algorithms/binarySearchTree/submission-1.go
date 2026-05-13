type TreeNode struct {
	Key   int
	Value int
	Left  *TreeNode
	Right *TreeNode
}

type TreeMap struct {
	Root *TreeNode
}

func NewTreeMap() *TreeMap {
	return &TreeMap{}
}

func (tm *TreeMap) Insert(key, val int) {
	var ordering func(newTree *TreeNode) *TreeNode

	ordering = func(newTree *TreeNode) *TreeNode{
		if newTree == nil {
			return &TreeNode{Key: key, Value: val}
		}

		if newTree.Key > key {
			newTree.Left = ordering(newTree.Left)
		} else if newTree.Key < key {
			newTree.Right = ordering(newTree.Right)
		} else {
			newTree.Value = val
		}
		
		return newTree
	}
	tm.Root = ordering(tm.Root)
}

func (tm *TreeMap) Get(key int) int {
	tmpTree := tm.Root
	for tmpTree != nil {
		if key == tmpTree.Key {
			return tmpTree.Value
		} else if key < tmpTree.Key {
			tmpTree = tmpTree.Left
		} else if key > tmpTree.Key {
			tmpTree = tmpTree.Right
		}
	}
	return -1
}

func (tm *TreeMap) GetMin() int {
	tmpTree := tm.Root

	if tmpTree == nil {
		return -1
	}

	for tmpTree.Left != nil {
		tmpTree = tmpTree.Left
	}
	return tmpTree.Value
}

func (tm *TreeMap) GetMax() int {
	tmpTree := tm.Root

	if tmpTree == nil {
		return -1
	}

	for tmpTree.Right != nil {
		tmpTree = tmpTree.Right
	}

	return tmpTree.Value
}

/*
func (tm *TreeMap) Remove(key int) { return }
*/

func (tm *TreeMap) Remove(key int) {
	var removal func(newTree *TreeNode, newKey int) *TreeNode

	removal = func(newTree *TreeNode, newKey int) *TreeNode {
		if newTree == nil {
			return nil
		}
		if newKey < newTree.Key {
			newTree.Left = removal(newTree.Left, newKey)
			return newTree
		} else if newTree.Key < newKey {
			newTree.Right = removal(newTree.Right, newKey)
			return newTree
		}

		// 0 or 1 child
		if newTree.Left == nil {
			return newTree.Right
		}
		if newTree.Right == nil {
			return newTree.Left
		}

		// 2 children
		successor := newTree.Right
		for successor.Left != nil {
			successor = successor.Left
		}
		nextKey := successor.Key
		newTree.Key, newTree.Value = successor.Key, successor.Value
		newTree.Right = removal(newTree.Right, nextKey)

		return newTree
	}
	tm.Root = removal(tm.Root, key)
}

func (tm *TreeMap) GetInorderKeys() []int {
	var out []int

	if tm.Root == nil {
		return out
	}
	inorder(tm.Root, &out)
	return out

}

func inorder(root *TreeNode, out *[]int) {
	if root == nil {
		return
	}

    inorder(root.Left, out)
	*out = append(*out, root.Key)
    inorder(root.Right, out)
}