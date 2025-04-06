class Stack:
    def factorial_stack(self,n):
        stack = []
        result = 1

        # Simulate recursive calls: push values down to 1
        while n > 1:
            stack.append(n)
            n -= 1

        # Unwind the stack: multiply as we return
        while stack:
            result *= stack.pop()

        return result

stk = Stack()
print(stk.factorial_stack(10))  # Output: 120
