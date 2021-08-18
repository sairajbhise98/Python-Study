# Linked List 

# Node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# For Linked List
class LinkedList:
    def __init__(self):
        self.head = None


    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_value, new_data):
        if self.head is None:
            print("List is empty!!!")
            return
        
        current =  self.head
        while current.next:
            if current.data == prev_value:
                break
            current = current.next

        if current.data == prev_value:
            new_node = Node(new_data)
            new_node.next = current.next
            current.next = new_node
        else:
            print('Given value not found in the list!!')
            return

    # Insert At End
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        # Reach to last Node
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    # Deleting the node
    def deleteNode(self, position):
        if self.head is None:
            print('List is empty!!')
            return
        
        temp = self.head
        if position == 0:
            self.head = temp.next 
            temp = None
            return
        
        # Find the key to be deleted
        for i in range(position -1):
            temp = temp.next 
            if temp is None:
                break
        
        # If Key is not present
        if temp is None or temp.next is None:
            print('Given postion is invalid !!')
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    # Search an element
    def search(self, key):
        current = self.head

        while current is not None:
            if current.data == key:
                print('List has ',key)
                return
            current = current.next
        print('Not Found')
        return

    # Bubble Sort
    def sortLinkedList(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + '->',end='')
            temp = temp.next



# Execution Part
LL = LinkedList()


def Push():
    data = int(input('Enter the data: '))
    print('Where you want to push the Item??')
    print('1) Start     2) End      3) After a number (Select number between 1-3)!!\n')
    choice = int(input('Your choice: '))
    if choice == 1:
        LL.insertAtBeginning(data)
    elif choice == 2:
        LL.insertAtEnd(data)
    elif choice == 3:
        LL.insertAfter(int(input('Enter the node: ')), data)
    else:
        print('Wrong input!!')

    LL.printList()
    return

def Delete():
    postion = int(input('Enter the Postion: '))
    LL.deleteNode(postion)
    LL.printList()
    return

def main():
    print('Hii\nWhat you want to do?\n1)Push    2)Pop   3)Search    4)Print List    5)Sort\n')
    print('Select number between 1-5')
    choice = int(input('You choice: '))
    if choice == 1:
        Push()
    if choice == 2:
        Delete()
    if choice == 3:
        LL.search(int(input('Enter the data: ')))
    if choice == 4:
        LL.printList()
    if choice == 5:
        LL.sortLinkedList(LL.head)
        LL.printList()
    
    print('\nDo you want to repeat?(y/n)')
    choice = input().upper()
    if choice == 'Y': main()
    

main()

