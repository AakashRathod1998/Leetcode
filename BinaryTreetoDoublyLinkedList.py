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

        # Approach 1
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

# Approach 2
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal last, first
            if node:
                # left
                helper(node.left)

                # node 
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node        
                last = node

                # right
                helper(node.right)
        
        if not root:
            return None
        
        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)

        # close DLL
        last.right = first
        first.left = last
        return first
