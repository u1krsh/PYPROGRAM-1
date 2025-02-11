from node import Node

def main():
    start, finish = 2, 5
    lst = Node(1)
    current = lst
    for i in range(start, finish):
        current.next = Node(i**3)  # Append a new node with the cube of i
        current = current.next  # Move to the new node
        
    current = lst  # Reset current to the head of the list
    while current is not None:
        print("Current node data:", current.data)
        current = current.next  # Move to the next node

if __name__ == "__main__":
    main()