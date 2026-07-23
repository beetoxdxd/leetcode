# Last updated: 22/7/2026, 11:35:11 p.m.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        h = {}
        for num in nums:
            h[num] = True

        dummy = ListNode()
        x = dummy

        while head:
            if not head.val in h: 
                x.next = head
                x = x.next
            head = head.next
        x.next = None
        return dummy.next