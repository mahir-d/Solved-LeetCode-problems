# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        toRtrn = ListNode()
        
        dummy = toRtrn
        carr = 0
        
        while l1 or l2:
            
            curr_l1 = l1.val if l1 else 0
            curr_l2 = l2.val if l2 else 0
            curr_sum = curr_l1 + curr_l2 + carr
            
            if curr_sum > 9:
                carr = 1
            else:
                carr = 0
                
            dummy.next = ListNode((curr_sum) % 10)
            
            
            l1 = None if not l1 or not l1.next else l1.next
            l2 = None if not l2 or not l2.next else l2.next
            dummy= dummy.next
            
        if carr == 1:
            dummy.next = ListNode(1)
        
        return toRtrn.next
            
        