'''
	Code By : Sairaj Bhise
	Topic : Data Structure and Algorithms (Linked List)
'''
class Linked_List :
	def __init__(self) :
		self.head = None

class Node : 
	def __init__(self,item) :
		self.item = item
		self.next = None

if __name__ == '__main__' :
	# Create Node
	linked_list = Linked_List()
	linked_list.head = Node(1)
	second = Node(2)
	third = Node(3)

	# Connect the Nodes
	linked_list.head.next = second
	second.next = third

	# Print List
	while linked_list.head != None :
		print(linked_list.head.item) 
		linked_list.head = linked_list.head.next
