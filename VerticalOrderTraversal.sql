
from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        # Dictionary to store vertical order of nodes
        vertical_order = defaultdict(list)

        # Queue for BFS traversal
        queue = deque([(root, 0)])  # (node, horizontal position)

        # Perform BFS traversal
        while queue:
            node, col = queue.popleft()
            vertical_order[col].append(node.val)
            print(vertical_order, col)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        # Sort the keys to ensure correct order
        sorted_cols = sorted(vertical_order.keys())

        # Construct the result by appending node values from the dictionary
        result = [vertical_order[col] for col in sorted_cols]

        return result
