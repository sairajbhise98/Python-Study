'''
	-------------------------------------------------------------
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (Tree Data Structure)
	-------------------------------------------------------------
'''

class Node:
	def __init__(self, item):
		self.item = item
		self.left = self.right = None

def checkDepth(node):
	d = 0
	while node is not None:
		d = d+1
		node = node.left
	return d

def isPerfectBinary(root, d, level = 0):
	# Check tree is empty or not
	if root is None:
		return True

	if root.left is None and root.right is None:
		return (d == level+1)

	if root.left is None or root.right is None:
		return False

	return (isPerfectBinary(root.left, d, level+1) and isPerfectBinary(root.right, d, level+1))

# Driver Code
if __name__ == '__main__':

	root = Node(2)
	root.left = Node(3)
	root.right = Node(4)
	root.left.left = Node(5)
	root.left.right = Node(6)

if isPerfectBinary(root, checkDepth(root)):
	print("It is Perfect binary tree.")
else:
	print("Its not Perfect binary tree.")