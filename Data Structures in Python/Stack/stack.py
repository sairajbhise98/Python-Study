'''
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (Stack)
	----------------------------------------------
	Points Covered in Code 
		1. Push 
		2. Pop
		3. Peek
'''

import array 
list1 = []
stack = array.array('i',list1)
# Top == -1 because currentle stack is empty
top = -1

def stack_push(element,stack) :
	'''
		1. if stack is full 
			1.1. print overflow
		2. else 
			2.1. push the element
			2.2. make the current element top and top ++
	'''
	pass

def stack_pop(stack) :
	'''
		1. if stack is empty 
			1.1. print underflow
		2. else 
			2.1. pop the element
			2.2. top --
	'''
	pass

def peek(stack) :
	'''
		1. if stack is empty 
			1.1. top = -1 
			1.1. return top 
		2. else 
			2.1. return current top element
	'''
	pass

def check_empty(stack) :
	'''
		1. if top = -1 
			1.1. true 
		2. else 
			2.1. false
	'''
	pass 

def check_full(stack) : 
	'''
		1. if top = max 
			1.1. return true
		2. else 
			2.1. return false
	'''
	pass

def show_stack(stack) :
	'''
		iterate through stack and print all the elements.
	'''
	pass
	

def execute(stack,top) :
	pass