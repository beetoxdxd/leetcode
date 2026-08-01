# Last updated: 1/8/2026, 5:27:51 p.m.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(node: Optional[TreeNode]) -> int:
            if node is None: return 0
            d_left = traverse(node.left)
            if d_left == -1: return -1
            d_right = traverse(node.right)
            if d_right == -1: return -1

            if abs(d_left - d_right) > 1: return -1
            return 1 + max(d_left, d_right)

        return traverse(root) != -1