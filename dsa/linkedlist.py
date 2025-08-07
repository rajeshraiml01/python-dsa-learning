class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def take_input():    
    while True:
        value = int(input("Enter value (or -1 to stop): "))
        if value == -1:
            break
        head = None
        while(value != -1):
            newNode = Node(value)
            if head is None:
                head = newNode
            else:
                temp = head
                while temp.next is not None:
                    temp = temp.next
                temp.next = newNode
            value = int(input("Enter next value (or -1 to stop): "))

    return head

def print_LL(head):
    if head is None:
        print("Linked List is empty")
        return
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


newhead = take_input()
print_LL(newhead)