def infix_to_postfix(infix_expression):
    stack = []
    postfix = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    infix_expression = infix_expression.replace(" ", "")  # Remove spaces

    for char in infix_expression:
        if char.isalnum():  # Operand (variable or number)
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(char, 0) and char != '^'):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

# Test
infix_expr = "(p+q)*r-s/t^u"
print("Infix Expression:", infix_expr)
postfix_expr = infix_to_postfix(infix_expr)
print("Postfix Expression:", postfix_expr)
