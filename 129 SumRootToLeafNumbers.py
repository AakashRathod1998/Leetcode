# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        queue = collections.deque()

        queue.append((root,0))
        tot = 0

        while queue:
            node, curr_val = queue.popleft()

            if node is None:
                continue

            curr_val = curr_val*10 + node.val

            if node.left is None and node.right is None:
                tot += curr_val
            else:
                queue.append((node.left, curr_val))
                queue.append((node.right, curr_val))

        return tot
