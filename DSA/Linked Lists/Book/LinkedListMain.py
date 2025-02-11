from LinkedList import LinkedList
def main():
    lst = LinkedList()
    
    while 1:
        choice = int(input("Choose 1 or 2: "))
        if(choice==1):
            value = eval(input("Enter a value: "))
            lst.insertBegin(value)
        elif(choice==2):
            break
if __name__ == "__main__":
    main()