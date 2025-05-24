# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        count = 0
        if root.left == None and root.right == None:
            return 1 + count
        elif root.right == None:
            count += 1
            self.maxDepth(root.left)
        elif root.left == None:
            count += 1
            self.maxDepth(root.right)
