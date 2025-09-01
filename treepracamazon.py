class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        arr = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        return arr[k - 1] if 1 <= k <= len(arr) else None