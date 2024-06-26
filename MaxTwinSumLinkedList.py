# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        curr = head
        max_tot = 0
        l1 = []
        while curr:
            l1.append(curr.val)
            curr = curr.next

        for i in range(int(len(l1)/2)):
            max_tot = max(max_tot, l1[i] + l1[-i-1])

        return max_tot

class Solution(object):
    def pairSum(self, head):
        current = head
        values = []

        while current:
            values.append(current.val)
            current = current.next
        
        i = 0
        j = len(values) - 1
        maximumSum = 0
        while(i < j):
            maximumSum = max(maximumSum, values[i] + values[j])
            i = i + 1
            j = j - 1
        
        return maximumSum


