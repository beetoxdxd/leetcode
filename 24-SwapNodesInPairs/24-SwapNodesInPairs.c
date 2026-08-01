// Last updated: 1/8/2026, 5:29:04 p.m.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    if(!head) return NULL;
    if(head->next == NULL) return head;
    
    struct ListNode *aux = head->next;
    head->next = swapPairs(aux->next);
    aux->next = head;
    head = aux;

    return head;
}