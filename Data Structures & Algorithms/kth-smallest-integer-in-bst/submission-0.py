# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.k = 0
        res = None
    def findKth(self, root):
        if not root:
            return

        self.findKth(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.findKth(root.right)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.findKth(root)
        return self.res