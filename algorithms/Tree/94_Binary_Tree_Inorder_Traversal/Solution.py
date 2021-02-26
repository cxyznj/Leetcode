# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        nodes = []
        while nodes or root:
            if root:
                nodes.append(root)
                root = root.left
            else:
                root = nodes.pop()
                res.append(root.val)
                root = root.right
        
        return res
