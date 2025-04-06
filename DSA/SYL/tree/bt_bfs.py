from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])  # start with the root node

    while queue:
        node = queue.popleft()  # remove from front
        result.append(node.val)

        # enqueue children
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Creating the binary tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(bfs(root))  # Output: [1, 2, 3, 4, 5, 6]
