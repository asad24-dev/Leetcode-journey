class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def printleftview(root):
    result = []
    visited = set()
    def dfs(root, depth):
        if not root:
            return None
        if depth not in visited:
            result.append(root.val)
            visited.add(depth)
        dfs(root.left, depth + 1)
        dfs(root.right, depth + 1)
    dfs(root, 0)
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.right.left = TreeNode(7)

print(printleftview(root))


#        1
#       / \
#      2   3
#     / \   \
#    4   5   6 
#       /
#      7   
# output: 1, 2, 4, 7
# 