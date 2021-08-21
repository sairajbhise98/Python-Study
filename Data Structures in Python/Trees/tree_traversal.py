'''
	-------------------------------------------------------------
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (Tree Data Structure)
	-------------------------------------------------------------
'''

# Create class
class Node:
	def __init__(self, item):
		self.left = None
		self.right = None
		self.val = item

# Inorder
def inorder(root):
	if root:
		inorder(root.left)
		print(str(root.val)+"->",end='')
		inorder(root.right)

# Pre Order 
def preorder(root):
	if root:
		print(str(root.val)+"->",end='')
		inorder(root.left)
		inorder(root.right)

# Post Order
def postorder(root):
	if root:
		inorder(root.left)
		inorder(root.right)
		print(str(root.val)+"->",end='')


# Driver code
if __name__ == '__main__':
	root = Node(2)
	root.left = Node(3)
	root.right = Node(4)
	root.left.left = Node(5)
	root.left.right = Node(6)

	# Inorder
	print('\nInorder Sequence: ')
	inorder(root)

	# Preorder
	print('\nPreorder Sequence: ')
	preorder(root)

	# Postorder
	print('\nPostorder Sequence: ')
	postorder(root)
