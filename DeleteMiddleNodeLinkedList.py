# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return
        
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next
        
        if n == 2:
            head.next = None
            return head    

        curr = head
        
        for i in range(n//2-1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head

# Approach 2:

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        # Edge case: return None if there is only one node.
        if head.next == None:
            return None
        
        # Initialize two pointers, 'slow' and 'fast'.
        slow, fast = head, head.next.next
        
        # Let 'fast' move forward by 2 nodes, 'slow' move forward by 1 node each step.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When 'fast' reaches the end, remove the next node of 'slow' and return 'head'.
        slow.next = slow.next.next
        
        # The job is done, return 'head'.
        return head
