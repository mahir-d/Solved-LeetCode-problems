# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2:
            return None
        
        if not l1 or not l2:
            return l1 or l2
        
        senital = ListNode(0, l1)
        prev = senital
        dummy = l1
        
        while l2:
            
            while dummy and dummy.val <= l2.val:
                prev = dummy
                dummy = dummy.next 
            
            if not dummy:
                prev.next = l2
                break
            else:
                temp = l2.next
                prev.next = l2
                l2.next = None
                l2.next = dummy
                dummy = l2
                l2 = temp
                
        return senital.next
                
                
        