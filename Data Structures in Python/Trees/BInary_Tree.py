'''
	-------------------------------------------------------------
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (Tree Data Structure)
	-------------------------------------------------------------
'''

class Node:
	def __init__(self,val):
		self.left = None
		self.right = None
		self.val = val

	def traverseInOrder(self):
		if self.left:
			self.left.traverseInOrder()
		print(str(self.val)+"->",end="")
		if self.right:
			self.right.traverseInOrder()

	def traversePreOrder(self):
		print(str(self.val)+"->",end="")
		if self.left:
			self.left.traverseInOrder()
		if self.right:
			self.right.traverseInOrder()

	def traversePostOrder(self):
		if self.left:
			self.left.traverseInOrder()
		if self.right:
			self.right.traverseInOrder()
		print(str(self.val)+"->",end="")

# Driver Code
if __name__ == '__main__':

	root = Node(2)
	root.left = Node(3)
	root.right = Node(4)
	root.left.left = Node(5)
	root.left.right = Node(6)

	# Inorder
	print('\nInorder Sequence: ')
	root.traverseInOrder()

	# Preorder
	print('\nPreorder Sequence: ')
	root.traversePreOrder()

	# Postorder
	print('\nPostorder Sequence: ')
	root.traversePostOrder()
