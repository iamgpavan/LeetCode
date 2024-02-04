/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1 == null){
            return list2;
        }
        
        if(list2 == null){
            return list1;
        }
        
        ListNode head = new ListNode(0);
        ListNode tempHead = head;
        ListNode temp1 = list1;
        ListNode temp2 = list2;
        
        while(temp1 != null && temp2 != null){
            // System.out.println(temp1.val);
            if(temp1.val < temp2.val){
                tempHead.next = temp1;
                temp1 = temp1.next;
            }else{
                tempHead.next = temp2;
                temp2 = temp2.next;
            }
            tempHead = tempHead.next;
        }
        
        if(temp1 != null){
            tempHead.next = temp1;
        }
        
        if(temp2 != null){
            tempHead.next = temp2;
        }
        
        return head.next;
        
    }
}