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
     class MyCmp{
        public:
            bool operator()(ListNode *l1,ListNode *l2){
                return l1->val>l2->val;
            }
    };
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue <ListNode*, vector<ListNode*>, MyCmp> pq;
        
        for(int i=0; i<lists.size(); i++){
            if(lists[i] != NULL){
                pq.push(lists[i]);
            }
        }
        
        ListNode* ans = new ListNode(-1);
        ListNode* temp = ans;
        
        while(!pq.empty()){
            ListNode* attach = pq.top();
            pq.pop();
            temp->next = attach;
            if(attach->next != NULL)
                pq.push(attach->next);
            temp = temp->next;
        }
        
        
        return ans->next;
    }
};