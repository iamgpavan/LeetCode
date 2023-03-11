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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    TreeNode *solve(ListNode *head, ListNode *end)
    {
        if (!head)
            return NULL;

        if (head == end)
            return NULL;

        int cnt = 0; ListNode *ptr = head;
        while(ptr != end)
        {
            cnt++;
            ptr = ptr->next;
        }
        int mid = cnt/2; ptr = head;
        ListNode *prev = NULL;
        while(mid--)
        {
            prev = ptr;
            ptr = ptr->next;
        }

        TreeNode *root = new TreeNode(ptr->val, solve(head, ptr), solve(ptr->next, end));
        return root;
    }

    TreeNode* sortedListToBST(ListNode* head) {
        return solve(head, NULL);
    }
};