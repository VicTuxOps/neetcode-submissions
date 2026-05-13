# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        newcnt = self.inorder(root)
        print(newcnt)
        if newcnt != -1:
            return True
        
        return False

    def inorder(self, root):
        if not root:
            return 0
        left = self.inorder(root.left)
        if left == -1:
            return -1
        right = self.inorder(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1