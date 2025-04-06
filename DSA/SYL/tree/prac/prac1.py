from collections import deque

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result



