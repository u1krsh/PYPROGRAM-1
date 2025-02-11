from node import Node

def main():
    lst = Node(20)
    lst.next = Node(30)
    lst.next.next = Node(25)
    print("lst: ",lst)
    print("list",lst.data)
    print("list.next: ",lst.next)
    print("list.next.data: ",lst.next.data)
    print("list.next.next: ",lst.next.next)
    print("list.next.next.data: ",lst.next.next.data)
if __name__ == "__main__":
    main()