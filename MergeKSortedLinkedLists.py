# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        ele = []

        for i in lists:
            curr = i
            while curr:
                ele.append(curr.val)
                curr = curr.next

        ele.sort()

        if not ele:
            return None

        lists = ListNode()
        curr = lists

        for i in range(len(ele)):
            if i == 0:
                lists.val = ele[i]
            else:
                curr.next = ListNode(ele[i])
                curr = curr.next
        

        return lists
