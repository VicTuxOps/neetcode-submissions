class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.node = None

    def _insert(self, root, key, val):
        if not root:
            return Node(key, val)
        if key > root.key:
            root.right = self._insert(root.right, key, val)
        elif key < root.key:
            root.left = self._insert(root.left, key, val)
        else:
            root.value = val
        return root

    def insert(self, key: int, val: int) -> None:
        self.node = self._insert(self.node, key, val)

    def get(self, key: int) -> int:
        if not self.node:
            return -1
        
        currNode = self.node
        while currNode:
            if key < currNode.key:
                currNode = currNode.left
            elif key > currNode.key:
                currNode = currNode.right
            else:
                return currNode.value
        
        return -1


    def _minValueNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    
    def getMin(self) -> int:
        if not self.node:
            return -1
        
        minNode = self._minValueNode(self.node)
        return minNode.value


    def getMax(self) -> int:
        if not self.node:
            return -1

        maxVal = self.node.value
        maxNode = self.node.right
        while maxNode:
            maxVal = maxNode.value
            maxNode = maxNode.right
        
        return maxVal

    def _remove(self, root, key):
        if not root:
            return None
        
        if key > root.key:
            root.right = self._remove(root.right, key)
        elif key < root.key:
            root.left = self._remove(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self._minValueNode(root.right)
                root.value = minNode.value
                root.key = minNode.key
                root.right = self._remove(root.right, minNode.key)
        
        return root

    def remove(self, key: int) -> None:
        if not self.node:
            return None
        
        self.node = self._remove(self.node, key)

    def _inorder(self, root, mylist):
        if not root:
            return
        
        self._inorder(root.left, mylist)
        mylist.append(root.key)
        self._inorder(root.right, mylist)

        return mylist

    def getInorderKeys(self) -> List[int]:
        if not self.node:
            return []
        return self._inorder(self.node, [])