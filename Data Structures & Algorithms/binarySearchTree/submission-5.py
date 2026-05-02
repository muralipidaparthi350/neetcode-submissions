class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not self.root:
            self.root = newNode

        else:
            curr = self.root
            prev = None
            
            while curr:
                prev = curr
                if newNode.key > curr.key:
                    curr = curr.right
                elif newNode.key < curr.key:
                    curr = curr.left
                else:
                    break

            if newNode.key > prev.key:
                prev.right = newNode
            elif newNode.key < prev.key:
                prev.left = newNode
            else:
                prev.val = newNode.val

    def get(self, key: int) -> int:
        curr = self.root

        while curr:
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left
            else:
                return curr.val

        return -1

    def getMin(self) -> int:
        curr = self.root
        if not curr:
            return -1
        while curr and curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        curr = self.root
        if not curr:
            return -1
        while curr and curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:

        def removeRec(node, key_):
            if not node:
                return None
            if key > node.key:
                node.right = removeRec(node.right, key_)
            elif key < node.key:
                node.left = removeRec(node.left, key_)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    curr = node.right
                    while curr and curr.left:
                        curr = curr.left
                    node.key = curr.key
                    node.val = curr.val
                    node.right = removeRec(node.right, key_)
                    return node

        self.root = removeRec(self.root, key)
        


    def getInorderKeys(self) -> List[int]:
        res = []
        def inorder(root):
            nonlocal res
            if not root:
                return

            inorder(root.left)
            res.append(root.key)
            inorder(root.right)

        inorder(self.root)
        return res



