# Last updated: 10/9/2026, 12:31:14 a.m.
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def averageOfSubtree(self, root: TreeNode) -> int:
9        def traverse(node: TreeNode) -> tuple:
10            num_nodes, total_sum, ans = 1, node.val, 0
11            if node.left: 
12                nodes, summ, partial_ans = traverse(node.left)
13                num_nodes += nodes
14                total_sum += summ
15                ans += partial_ans
16
17            if node.right: 
18                nodes, summ, partial_ans = traverse(node.right)
19                num_nodes += nodes
20                total_sum += summ
21                ans += partial_ans
22
23            if total_sum // num_nodes == node.val: ans += 1
24            return (num_nodes, total_sum, ans)
25
26        return traverse(root)[2]