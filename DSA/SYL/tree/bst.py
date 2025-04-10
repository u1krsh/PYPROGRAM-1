class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)

root = None
for val in [8, 3, 10, 1, 6, 14, 4, 7]:
    root = insert(root, val)

print("Inorder Traversal (Sorted):")
inorder(root)  # Output: 1 3 4 6 7 8 10 14

