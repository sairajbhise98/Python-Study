'''
	-------------------------------------------------------------
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (Tree Data Structure)
	-------------------------------------------------------------
'''

class Node:
	def __init__(self,item):
		self.item = item
		self.left = self.right = None

class _CalculateHeight_:
	def __init__(self):
		self.CalculateHeight = 0

def isBalanced(root, CalculateHeight):
	leftHeight = _CalculateHeight_()
	rightHeight = _CalculateHeight_()

	if root is None:
		return True

	l = isBalanced(root.left, leftHeight)
	r = isBalanced(root.right, rightHeight)

	CalculateHeight.CalculateHeight = max(leftHeight.CalculateHeight, rightHeight.CalculateHeight) + 1

	if abs(leftHeight.CalculateHeight - rightHeight.CalculateHeight) <= 1:
		return l and r

	return False

# Driver Code
if __name__ == '__main__':

	CalculateHeight = _CalculateHeight_()

	root = Node(2)
	root.left = Node(3)
	root.right = Node(4)
	root.left.left = Node(5)
	root.left.right = Node(6)

if isBalanced(root, CalculateHeight):
	print("It is Perfect binary tree.")
else:
	print("Its not Perfect binary tree.")