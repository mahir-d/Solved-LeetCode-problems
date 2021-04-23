# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head: ListNode) -> ListNode:
            
        pointer = head
        prev = None
        while pointer:
            
            temp = pointer.next
            pointer.next = prev
            
            prev = pointer
            pointer = temp
            
        return prev
             