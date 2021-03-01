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
    ListNode* sortList(ListNode* head) {
        if(!head || !head->next) {
            return head;
        }
        ListNode *midNode = splitList(head);
        ListNode *leftsortNode = sortList(head);
        ListNode *rightsortNode = sortList(midNode);
        return mergeList(leftsortNode, rightsortNode);
    }
    
    ListNode* splitList(ListNode *head) {
        ListNode *preMid = nullptr;
        while(head && head->next) {
            preMid = (preMid)? preMid->next : head;
            head = head->next->next;
        }
        // cut the LinkedList
        ListNode* mid = preMid->next;
        preMid->next = nullptr;
        return mid;
    }
    
    ListNode* mergeList(ListNode *lNode, ListNode *rNode) {
        ListNode *head = new ListNode;
        ListNode *tail = head;
        while(lNode && rNode) {
            if(lNode->val < rNode->val) {
                tail->next = lNode;
                lNode = lNode->next;
                tail = tail->next;
            }
            else {
                tail->next = rNode;
                rNode = rNode->next;
                tail = tail->next;
            }
        }
        // traverse till the end of merged list when one of list do not finish the traverse
        tail->next = (lNode)? lNode : rNode;
        return head->next;
    }
        
};
