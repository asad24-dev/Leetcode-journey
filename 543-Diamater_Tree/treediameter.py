# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.maxdepth = 0
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            self.maxdepth = max(self.maxdepth, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.maxdepth
                
        