# Last updated: 1/8/2026, 5:29:13 p.m.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        aux = head
        h = []
        cont = 0
        while aux:
            h.append(aux)
            aux = aux.next
            cont += 1

        if cont-n-1 < 0: return head.next
        node = h[cont-n-1]
        node.next = node.next.next
        return head