class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        diff = float('inf')
        prev = None
        def dfs(node):
            nonlocal diff, prev
            if not node:
                return
            dfs(node.left)
            if prev:
                diff = min(diff, node.val - prev.val)
            prev = node
            dfs(node.right)
        dfs(root)
        return diff
#[90,69,null,49,89,null,52]
tree = TreeNode(90)
tree.left = TreeNode(69)
tree.left.left = TreeNode(49)
tree.left.right = TreeNode(89)
tree.left.left.right = TreeNode(52)

print(Solution().minDiffInBST(tree))