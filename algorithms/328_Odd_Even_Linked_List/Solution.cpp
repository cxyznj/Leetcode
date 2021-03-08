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
    ListNode* oddEvenList(ListNode* head) {
        if(!head) {
            return head;
        }
        ListNode *evenhead = head->next;
        ListNode *oddp = head, *evenp = evenhead;
        while(oddp->next && evenp->next) {
            oddp->next = evenp->next;
            oddp = evenp->next;
            evenp->next = oddp->next;
            evenp = oddp->next;
        }
        oddp->next = evenhead;
        return head;
    }
};
