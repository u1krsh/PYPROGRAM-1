def move_disk(from_rod, to_rod, from_stack, to_stack):
    disk = from_stack.pop()
    to_stack.append(disk)
    print(f"Move disk {disk} from {from_rod} to {to_rod}")

def hanoi(n, source, auxiliary, target, source_stack, auxiliary_stack, target_stack):
    if n == 1:
        move_disk(source, target, source_stack, target_stack)
        return
    hanoi(n - 1, source, target, auxiliary, source_stack, target_stack, auxiliary_stack)
    move_disk(source, target, source_stack, target_stack)
    hanoi(n - 1, auxiliary, source, target, auxiliary_stack, source_stack, target_stack)

# Setup for 3 disks
n = 3
A = list(reversed(range(1, n + 1)))  # Source rod as a stack (top of stack is last item)
B = []
C = []

print("Initial State:")
print("A:", A)
print("B:", B)
print("C:", C)

hanoi(n, 'A', 'B', 'C', A, B, C)

print("\nFinal State:")
print("A:", A)
print("B:", B)
print("C:", C)
