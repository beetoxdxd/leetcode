# Last updated: 1/8/2026, 5:28:06 p.m.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        aux = head
        n = 0
        while aux:
            aux = aux.next
            n += 1

        if not head: return head
        k %= n
        if k == 0: return head # no change

        aux = head
        prev = None
        for i in range(n - k):
            prev = aux
            aux = aux.next

        prev.next = None
        prev = aux
        
        while aux.next:
            aux = aux.next

        aux.next = head
        head = prev

        return head