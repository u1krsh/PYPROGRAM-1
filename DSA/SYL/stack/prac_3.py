def infix_to_postfix(infix_expr):
    stack = []
    postfix_expr = ""
    precedence = {'+':1,'-':1,"*":2,'/':2,"^":3}

    for char in infix_expr.replace(" ",""):
        if char.Isalnum():
            postfix_expr += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_expr += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] and precedence.get(stack[-],0) >= precedence.get(char,0):
                postfix_expr += stack.pop()
            stack.append(char)

    while stack:
        postfix_expr += stack.pop()

    return postfix_expr

