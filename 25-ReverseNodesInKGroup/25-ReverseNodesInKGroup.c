// Last updated: 1/8/2026, 5:29:02 p.m.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverse(struct ListNode* t, int k, struct ListNode *p){
    struct ListNode *prev = p, *next;

    for(int i = 0; i < k; i++){
        next = t->next;
        t->next = prev; prev = t;
        t = next;
    } 

    return prev;
}

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    struct ListNode *aux = head;
    for(int i = 0; i < k; i++){
        if(aux == NULL) return head;
        aux = aux->next;
    }


    aux = reverseKGroup(aux, k);
    head = reverse(head, k, aux);
    return head;
}