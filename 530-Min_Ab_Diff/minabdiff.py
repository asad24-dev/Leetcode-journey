# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        global prev, minDist
        prev = None
        minDist = float('inf')
        def dfs(node):
            global prev, minDist
            if not node:
                return
            dfs(node.left)
            if prev is not None:
                minDist = min(minDist, node.val - prev)
            prev = node.val
            dfs(node.right)
        dfs(root)
        return minDist
