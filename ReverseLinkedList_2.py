# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        ptr = head
        li, rev_list = [], []
        i = 0
        
        while ptr:

            if i < left - 1 or i >= right:
                li.append(ptr.val)
            elif i >= left - 1 and i < right:
                rev_list.append(ptr.val)
            else:
                print('pass')
                pass
            
            # print(i, left, right)
            # print(ptr.val)

            ptr = ptr.next
            i += 1

        # print('li', li)
        # print('rev_list', rev_list) 

        new_li = li[:left - 1] + rev_list[::-1] + li[left - 1:]
        print(new_li)
        # print() 

        ptr1 = ListNode(new_li[0])
        ptr2 = ptr1

        for i in new_li[1:]:
            node = ListNode(i)
            ptr1.next = node
            ptr1 = ptr1.next
        
        return ptr2
