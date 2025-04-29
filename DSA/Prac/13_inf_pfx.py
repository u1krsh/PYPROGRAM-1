def infix_to_postfix(inf):
    postfix_expr = ""
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for char in inf.replace(" ",""):
        if char.isalnum():
            postfix_expr += char
        if char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                postfix_expr += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "(" and precedence.get(stack[-1],0) >= precedence.get(char,0):
                postfix_expr += stack.pop()
            stack.append(char)

        while stack:
            postfix_expr += stack.pop()

    return postfix_expr
