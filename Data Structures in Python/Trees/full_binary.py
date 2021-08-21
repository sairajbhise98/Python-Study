'''
	-------------------------------------------------------------
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (Tree Data Structure)
	-------------------------------------------------------------
'''

class Node:
	def __init__(self, item):
		self.item = item
		self.left = None
		self.right = None

# Check tree is Full Binary Tree or not
def isFullBinary(root):
	# Tree empty condition
	if root.item == None:
		return True

	# Check for other nodes
	if root.left is None and root.right is None:
		return True
	if root.left is not None and root.right is not None:
		return (isFullBinary(root.left) and isFullBinary(root.right))

	return False

# Driver Code
if __name__ == '__main__':

	root = Node(2)
	root.left = Node(3)
	root.right = Node(4)
	root.left.left = Node(5)
	root.left.right = Node(6)

if isFullBinary(root):
	print("It is full binary tree.")
else:
	print("Its not full binary tree.")