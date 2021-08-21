'''
	-------------------------------------------------------------
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (Complete Binary Tree)
	-------------------------------------------------------------
'''
class Node :
	def __init__(self,item) :
		self.item = item 
		self.left = None
		self.right = None

	# Count the number of Nodes
	def count_nodes(self,root) :
		if root is None :
			return 0
		return (1 + self.count_nodes(root.left) + self.count_nodes(root.right))

	# Check if tree is complete binary tree or not
	def is_complete(self,root,index,numberNodes) :
		# check if tree is empty
		if root is None :
			return True 
		if index >= numberNodes :
			return False
		return (self.is_complete(root.left,2*index+1,numberNodes) and self.is_complete(root.right,2*index+2,numberNodes))

# Create Tree using Node Class

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

node_count = root.count_nodes(root)
index = 0 

if root.is_complete(root,index,node_count) :
	print('Yes the tree is Complete')
	print('Node count is :',node_count)
else :
	print('No its not complete')