# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prevHead: "ListNode" = None
        currHead: "ListNode" = head
        
        while currHead:
            temp: "ListNode" = currHead.next
            
            currHead.next = prevHead
            prevHead = currHead 
            currHead = temp
            
        return prevHead
        
        
