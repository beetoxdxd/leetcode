# Last updated: 1/8/2026, 5:24:47 p.m.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return root
        arr = []

        def traverse(node: Optional[TreeNode]) -> None:
            if node.left: traverse(node.left)
            arr.append(node.val)
            if node.right: traverse(node.right)

        traverse(root)

        def construct(i: int, j: int) -> Optional[TreeNode]:
            if i > j: return None
            h = (i+j) // 2
            node = TreeNode(arr[h])
            node.left = construct(i, h-1)
            node.right = construct(h+1, j)
            return node

        return construct(0, len(arr)-1)