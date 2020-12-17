# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        my_stack: List[ListNode] = []
            
        currHead = head
        
        while currHead.next != None:
            my_stack.append(currHead)
            currHead = currHead.next
        
        val: int = currHead.val + 1
            
        if val > 9:
            carr = 1
            currHead.val = 0
            while len(my_stack) != 0 and carr != 0:
                currHead = my_stack.pop()
                val = currHead.val + carr
                if val > 9:
                    val = 0
                    carr = 1
                    currHead.val = val
                else: 
                    carr = 0
                    currHead.val = val
            if carr == 1:
                newHead: ListNode = ListNode(1, head)
                return newHead
            return head
                
                
