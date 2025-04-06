from anaconda_project.internal.conda_api import result


class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def pre_order(root):
    if not root:
        return []
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def in_order(root):
    if not root:
        return []

    stack = []
    result = []
    current = root

    while current or stack:
        while stack:
            stack.append(current)
            current = current.left

    current = stack.pop()
    result.append(current.val)
    current= current.right

    return result

def post_order(root):
    if not root:
        return []

    stack1 = [root]
    stack2 = []
    result = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.right:
            stack1.append(node.right)
        if node.left:
            stack1.append(node.left)

    while stack2:
        result.append(stack2.pop().val)
    return result