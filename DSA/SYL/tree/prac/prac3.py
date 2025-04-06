class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insert(root,val):
    if not root:
        return Node(val)

    if val < root.val:
        root.left = insert(root.left,val)
    else:
        root.right = insert(root.right,val)
    return root

def inorder(root):
    if not root:
        return  []
    inorder(root.left)
    print(root.val,end="")
    inorder(root.right)