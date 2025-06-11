# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isSametree(r, s):
            if not r and not s:
                return True
            if not r or not s:
                return False
            if r.val != s.val:
                return False
            if r.val == s.val and isSametree(r.left, s.left) and isSametree(r.right, s.right):
                return True

        def dfs(root, subRoot):
            if not root:
                return False
            if isSametree(root, subRoot):
                return True
            else:
                return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)


        