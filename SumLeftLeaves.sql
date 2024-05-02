# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        queue = collections.deque([(root, False)])
        sum_leaf = 0

        while queue: 

            node, is_left = queue.popleft()
            print(node.val)

            if is_left == True and not node.left and not node.right:
                sum_leaf += node.val
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
        
        return sum_leaf
