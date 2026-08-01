# Last updated: 1/8/2026, 5:25:11 p.m.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode], num: int) -> int:
            if node is None: return 0
            num = (num << 1) | node.val
            
            if node.left == node.right: return num
            return traverse(node.left, num) + traverse(node.right, num)

        return traverse(root, 0)

