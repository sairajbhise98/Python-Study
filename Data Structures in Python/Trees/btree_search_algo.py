'''
	-------------------------------------------------------------
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (B-Tree Search Algorithm)
	-------------------------------------------------------------
'''

# Algorithm
"""

	BTreeSearch(x, k):
		i = 1
		while i <= n[x] and k >= key i[x]:
			i = i+1
		if i = n[x] and k = keyi[x]:
			then return (x,i)
		if leaf[x] :
			then return NIL
		else :
			return BtreeSearch(ci[x], k)

"""

class BTreeNode:
	def __init__(self, leaf = False):
		self.leaf = leaf
		self.keys = []
		self.child = []

class BTree :
	def __init__(self, t):
		self.root = BTreeNode(True)
		self.t = t
	def print_tree(self, x, l=0):
		print("Level ",l ," ",len(x.keys), end=" : ")
		for i in x.keys:
			print(i, end = " ")
			print()
			l = l+1
			if len(x.child) > 0:
				for i in x.child:
					self.print_tree(i,l)
	def search_key(self, k, x = None):
		if x is not None:
			i = 0
			while i< len(x.keys) and k>x.keys[i][0]:
				i = i + 1
			return (x,i)
		elif x.leaf:
			return None
		else: return self.search_key(k, self.root)
