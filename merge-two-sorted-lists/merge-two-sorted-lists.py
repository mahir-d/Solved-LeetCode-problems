# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        dummy: ListNode = ListNode(0, l1)
            
        pointer = dummy
        
        while pointer.next != None:
            
            if l2 != None:
                while pointer.next != None and l2.val > pointer.next.val:
                    pointer = pointer.next
                
                temp1 = pointer.next    
                temp = l2.next
                pointer.next = l2
                l2.next = temp1
                l2 = temp
                
            else:
                break
                
                
        return dummy.next
                
        
        
