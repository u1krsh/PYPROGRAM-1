from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value,end="-")
        if self.right:
            self.right.PrintTree()

def bfs(root):
    if not root:
        return

    queue = deque([root])  # Initialize queue with root
    while queue:
        node = queue.popleft()  # Dequeue front element
        print(node.value, end=" ")  # Process node

        if node.left:
            queue.append(node.left)  # Enqueue left child
        if node.right:
            queue.append(node.right)  # Enqueue right child

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
root.PrintTree()
print()
print("BFS Traversal:")
bfs(root)
