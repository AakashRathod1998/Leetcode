from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        # Dictionary to store vertical order of nodes
        vertical_order = defaultdict(list)

        # Queue for BFS traversal
        queue = deque([(root, 0, 0)])  # (node, horizontal position, vertical position)

        # Perform BFS traversal
        while queue:
            node, col, lvl = queue.popleft()
            vertical_order[col].append((lvl, node.val))
            # print(vertical_order, col)

            if node.left:
                queue.append((node.left, col - 1, lvl + 1))
            if node.right:
                queue.append((node.right, col + 1, lvl + 1))
            
            # print(vertical_order)

        # Sort the keys to ensure correct order
        sorted_cols = sorted(vertical_order.keys())

        # Construct the result by appending node values from the dictionary
        result = [sorted(vertical_order[col]) for col in sorted_cols]

        op = []

        for i in result: 
            op.append([j[1] for j in i])
        print(op)

        return op 
