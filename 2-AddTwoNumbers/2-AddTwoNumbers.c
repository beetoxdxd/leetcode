// Last updated: 1/8/2026, 5:29:43 p.m.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *x = malloc(sizeof *x), *aux, *begin = x;
    int carry = 0, total = 0;

    while(l1 || l2 || carry){
        total = carry;

        if(l1){
            total += l1->val;
            l1 = l1->next;
        }
        
        if(l2){
            total += l2->val;
            l2 = l2->next;
        }

        carry = total / 10;
        x->val = total % 10;
        x->next = malloc(sizeof *x);
        aux = x; x = x->next; 
    }
    
    
    free(x);
    aux->next = NULL;
    return begin;
}