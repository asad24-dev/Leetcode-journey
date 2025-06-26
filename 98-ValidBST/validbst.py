# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(node, min, max):
            if not node:
                return True
            if not (min < node.val < max):
                return False
            return dfs(node.left, min, node.val) and dfs(node.right, node.val, max)
        
        return dfs(root, float('-inf'), float('inf'))
