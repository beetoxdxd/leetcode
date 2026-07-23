# Last updated: 22/7/2026, 11:36:17 p.m.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        stack = []

        while head:
            stack.append(head.val)
            head = head.next

        for i in range(len(stack)//2):
            ans = max(ans, stack[i]+stack[-i-1])

        return ans