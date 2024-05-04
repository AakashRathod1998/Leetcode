# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next or not head.next.next:
            return head

        odd_ptr = head
        even_ptr = head.next

        even_start = even_ptr

        curr = head.next.next

        while curr:

            odd_ptr.next = curr
            odd_ptr = odd_ptr.next
            curr = curr.next

            if curr:
                even_ptr.next = curr
                even_ptr = even_ptr.next
                curr = curr.next
            else:
                break

        even_ptr.next = None
        odd_ptr.next = even_start

        return head
