# Last updated: 1/8/2026, 5:29:05 p.m.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            head = ListNode()
            aux = head
            while list1 and list2:
                if list1.val < list2.val:
                    aux.next = list1
                    aux = aux.next
                    list1 = list1.next
                else:
                    aux.next = list2
                    aux = aux.next
                    list2 = list2.next

            if list1: aux.next = list1
            else: aux.next = list2

            return head.next

        if not lists: return None
        while len(lists) > 1:
            proximas_listas = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                proximas_listas.append(merge(l1, l2))
            lists = proximas_listas

        return lists[0]