# Last updated: 1/8/2026, 5:24:11 p.m.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtrees = []

        def traverse(node: Optional[TreeNode]) -> int:
            left, right = 0, 0
            if node.left: left = traverse(node.left)
            if node.right: right = traverse(node.right)

            subtrees.append(node.val + left + right)
            return node.val + left + right

        ans = 0
        total_sum = traverse(root)
        
        for subtree in subtrees:
            ans = max(ans, (total_sum - subtree) * subtree)

        return ans % (10**9 + 7)