def infix_to_postfix(infix_expression):
    stack = []
    postfix_expression = ""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for char in infix_expression.replace(" ", ""):
        if char.isalnum():  # Operand
            postfix_expression += char
        elif char == '(':  # Left Parenthesis
            stack.append(char)
        elif char == ')':  # Right Parenthesis
            while stack and stack[-1] != '(':
                postfix_expression += stack.pop()
            stack.pop()  # Remove '('
        else:  # Operator
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                postfix_expression += stack.pop()
            stack.append(char)

    while stack:
        postfix_expression += stack.pop()

    return postfix_expression


# Test it
infix_expr = "a + b * (c ^ d - e) / f"
postfix_expr = infix_to_postfix(infix_expr)
print("Infix Expression:", infix_expr)
print("Postfix Expression:", postfix_expr)
