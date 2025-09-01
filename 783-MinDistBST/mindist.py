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
        def dfs(node):
            nonlocal diff
            if not node:
                return
            dfs(node.left)
            if node.left:
                diff = min(diff, node.val - node.left.val)
            if node.right:
                diff = min(diff, node.right.val - node.val)
            dfs(node.right)
        dfs(root)
        return diff
#[1,0,48,null,null,12,49]
tree = TreeNode(9)
tree.left = TreeNode(0)
tree.right = TreeNode(48)
tree.right.left = TreeNode(12)
tree.right.right = TreeNode(56)

print(Solution().minDiffInBST(tree))