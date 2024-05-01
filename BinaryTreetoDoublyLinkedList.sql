"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return

        curr = root
        l1 = [root.val]

        def dfs(root, l1):
            if not root:
                return
            if root.left:
                l1.append(dfs(root.left, l1))
            if root.right:
                l1.append(dfs(root.right, l1))
            return root.val

        dfs(root, l1)
        
        l1 = sorted(l1)

        head = Node(l1[0])
        curr1 = head
        curr2 = head

        for i in l1[1:]:
            temp = Node(i)
            curr1.right = temp
            curr1 = curr1.right
            curr1.left = curr2
            curr2 = curr2.right
        
        curr1.right = head
        head.left = curr1


        return head
