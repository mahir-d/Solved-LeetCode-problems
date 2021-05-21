# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        
        dummy = ListNode()
        dummy.next = head
        
        slow = head
        fast = head
        
        for _ in range(n):
            
            fast = fast.next
            
        
        
        prev = dummy
        
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            
        prev.next = slow.next
        return dummy.next
        
            
        
        
            
        