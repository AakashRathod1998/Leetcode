class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

Approach 2:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ele = []

        curr1 = list1
        while curr1:
            ele.append(curr1.val)
            curr1 = curr1.next

        curr1 = list2
        while curr1:
            ele.append(curr1.val)
            curr1 = curr1.next
        ele.sort()
        
        if not ele:
            return None
        list1 = ListNode()
        curr1 = list1

        for i in range(len(ele)):
            if i == 0:
                curr1.val = ele[i]
                pass
            else:
                curr1.next = ListNode(ele[i])
                curr1 = curr1.next
        
        return list1
