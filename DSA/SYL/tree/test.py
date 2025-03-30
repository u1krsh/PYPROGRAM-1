precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
print(precedence.get('_',2))  # Output: 1