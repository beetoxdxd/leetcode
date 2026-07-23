# Last updated: 22/7/2026, 11:36:19 p.m.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None
        
        one = head
        two = head.next

        while two.next and two.next.next:
            one = one.next
            two = two.next.next

        one.next = one.next.next
        return head