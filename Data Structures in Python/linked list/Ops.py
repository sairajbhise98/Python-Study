'''
    Code by : Sairaj Bhise
    Topic : Data Structure and Algorithms (Ops on Linked List)
'''

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 1

    # Insert at the beginning
    def insertAtBeginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        self.count = self.count + 1

    # Insert after a node
    def insertAfter(self, node, data):
        new_node = Node(data)
        temp_node = self.head
        for i in range(node) :
            if(temp_node.next) :
                temp_node = temp_node.next

        new_node.next = temp_node.next
        temp_node.next = new_node
        self.count = self.count + 1

        '''
        if node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        '''

    # Insert at the end
    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next is not None):
            last = last.next

        last.next = new_node
        self.count = self.count + 1

    # Deleting a node
    def deleteNode(self, position):

        if self.head == None:
            return

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            temp_node = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp_node = temp_node.next
            if temp_node is None:
                break

        # If the key is not present
        if temp_node is None:
            return

        if temp_node.next is None:
            return

        next = temp_node.next.next
        temp_node.next = None
        temp_node.next = next

        self.count = self.count - 1

    def printList(self):
        temp_node = self.head
        while (temp_node):
            print(str(temp_node.item) + " ", end="--->")
            temp_node =temp_node.next

    # Reversing the Node
    def reverse(self) :
        prev = None 
        current = self.head
        next_ = None 
        while (current is not None) :
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.head = prev

    # Search for item in Linked List
    def searchItem(self,key_) :
        temp_count_ = 0
        current = self.head
        while(current is not None) :
            if current.item == key_ :
                print('Success!',end=' ')
                temp_count_ = temp_count_ + 1
                return temp_count_
            current = current.next
            temp_count_ = temp_count_ + 1
        return False

    # Sort the linked List (Merge Sort)
    '''
            3 Steps :
                1) Get middle 
                2) Divide the list into two halve and sort each list independently 
                3) Merge the lists recursively to get final output
    ''' 
    # merge the Lists
    def sortedMerge(self,a,b) :
        # Initialise result
        result = None

        # Base case
        if a == None:
            return b
        if b == None:
            return a
        # Pick either a or b and recursse
        if a.item <= b.item :
            result = a
            result.next = self.sortedMerge(a.next,b)
        else :
            result = b
            result.next = self.sortedMerge(a,b.next)
        return result

    # Merge Sort
    def mergeSort(self,h) :
        # Base case is head is None :
        if h == None or h.next == None:
            return h

        # get middle of the list
        middle = self.getMiddle(h)
        nexttomiddle = middle.next

        # set middle.next to None 
        # this will create left list
        middle.next = None

        # Apply merge sort on left 
        left = self.mergeSort(h)

        # Apply merege sort on right
        right = self.mergeSort(nexttomiddle)

        # merge the list
        sorted_list = self.sortedMerge(left,right)
        return sorted_list

    # get Middle
    def getMiddle(self, head) :
        # Return None if head is None
        if (head == None) :
            return None

        # Imp logic
        slow = head
        fast = head

        # while fast goes two steps, slow will take one step
        # ultimatly slow will be at middle
        while(fast.next != None and fast.next.next != None) :
            slow = slow.next
            fast = fast.next.next
        return slow




if __name__ == '__main__':

    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtEnd(4)
    llist.insertAfter(1, 5)

    print('Linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.deleteNode(4)
    llist.printList()
    print('\nNode Count: ',llist.count)
    print('\nLinked after reversing: ')
    llist.reverse()
    llist.printList()

    # search for item
    print('\n\nSearching for 3 in Linked List')
    n = llist.searchItem(3)
    if(n) :
        print("Given data is present at index: ",n)
    else :
        print('Given key is not present in Linked List')

    llist.mergeSort(llist.head)
    print('\nSorted List: ',end='')
    llist.printList()
    print('\n')


