# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        head1 = ListNode(0)
        head2 = ListNode(0)
        
        dummy = head
        
        d1 = head1
        d2 = head2
        
        
        temp = None
        while dummy:
            
            if dummy.val < x:
                d1.next = dummy
                temp = dummy.next
                dummy.next = None
                d1 = d1.next
            else:
                d2.next = dummy
                temp = dummy.next
                dummy.next = None
                d2 = d2.next
                
            dummy = temp
            
            
        d1.next = head2.next
        return head1.next