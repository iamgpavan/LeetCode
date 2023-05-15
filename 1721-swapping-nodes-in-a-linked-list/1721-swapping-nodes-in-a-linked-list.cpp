/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* curr = head, *first, *second = head;
        for(int i = 0; i < k; i++) first = curr, curr = curr->next;
        while(curr){
            second = second->next;
            curr = curr->next;
        }
        swap(first->val, second->val);
        return head;
    }
};