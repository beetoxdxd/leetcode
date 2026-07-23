# Last updated: 22/7/2026, 11:36:08 p.m.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        a, b = 0, 0

        for parent, child, isLeft in descriptions:
            if parent not in nodes: 
                parent_node = TreeNode(val = parent)
                nodes[parent] = parent_node
                a += parent
            else: parent_node = nodes[parent]

            if child not in nodes: 
                child_node = TreeNode(val = child)
                nodes[child] = child_node
                a += child
            else: child_node = nodes[child]

            if isLeft: parent_node.left = child_node
            else: parent_node.right = child_node

            b += child

        return nodes[a-b]