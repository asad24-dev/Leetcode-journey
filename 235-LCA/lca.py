# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
# LCA is the first number in a bst between the given parameters p and q.
# If both p and q are less than root, then LCA is in the left subtree
# If both p and q are greater than root, then LCA is in the right subtree
# If p and q are on different sides of root, then root is the LCA