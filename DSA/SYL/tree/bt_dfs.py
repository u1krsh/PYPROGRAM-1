class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
#(Root → Left → Right)
def preorder_iterative(root):
    if not root:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
# (Left → Root → Right)
def inorder_iterative(root):
    stack = []
    result = []
    current = root

    while current or stack:
        # Go as left as possible
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
# (Left → Right → Root)
def postorder_iterative(root):
    if not root:
        return []

    stack1 = [root]
    stack2 = []
    result = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        result.append(stack2.pop().val)

    return result
# Tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder:", preorder_iterative(root))   # [1, 2, 4, 5, 3]
print("Inorder:", inorder_iterative(root))     # [4, 2, 5, 1, 3]
print("Postorder:", postorder_iterative(root)) # [4, 5, 2, 3, 1]
