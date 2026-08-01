// Last updated: 1/8/2026, 5:29:09 p.m.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if(!list1) return list2;
    if(!list2) return list1;

    if(list2->val > list1->val){
        list1->next = mergeTwoLists(list1->next, list2);
        return list1;
    }
    
    list2->next = mergeTwoLists(list1, list2->next);
    return list2;
}