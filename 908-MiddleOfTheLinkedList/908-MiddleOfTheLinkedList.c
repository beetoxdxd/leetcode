// Last updated: 1/8/2026, 5:25:32 p.m.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode *aux = head;

    while(aux != NULL){
        aux = aux->next;
        if(aux){
            aux = aux->next;
            head = head->next;
        }
    }

    return head;
}