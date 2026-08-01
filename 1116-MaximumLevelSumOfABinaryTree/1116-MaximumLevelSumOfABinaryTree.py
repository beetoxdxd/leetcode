# Last updated: 1/8/2026, 5:25:07 p.m.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(int)

        def dfs(node: Optional[TreeNode], level: int) -> None:
            dic[level] += node.val
            if node.left: dfs(node.left, level+1)
            if node.right: dfs(node.right, level+1)

        dfs(root, 1)
        return min(k for k, v in dic.items() if v == max(dic.values()))