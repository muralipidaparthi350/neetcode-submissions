# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minVal(self, root):
        curr = root

        while curr and curr.left:
            curr = curr.left

        return curr.val

    def remove(self, root, value):
        if not root:
            return None

        if value > root.val:
            root.right = self.remove(root.right, value)
        elif value < root.val:
            root.left = self.remove(root.left, value)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minValue = self.minVal(root.right)
                root.val = minValue
                root.right = self.remove(root.right, minValue)

        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.remove(root, key)