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
    ListNode* swapPairs(ListNode* head) {
        // A: it will gives head of node after swapping all adj nodes
        
        if(head == NULL || head->next == NULL)  return head;
        
        ListNode* temp = NULL;
        ListNode* temp2 = head;
        ListNode* head2 = head;
        int i = 0;
        while(i<2){
            head2 = head2->next;
            temp2->next = temp;
            temp = temp2;
            temp2 = head2;
            i+=1;
        }
        
        head->next = swapPairs(head2);
        
        return temp;
        
        
    }
};