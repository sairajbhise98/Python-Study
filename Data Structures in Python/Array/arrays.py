'''

	Code By : Sairaj Bhise
	Topic : Data Structures - Array
	Date : 30-12-2020

	-----------------------------------------------
	In this array.py code I have demonstrated basic operations 
	that you can perform on Arrays i.e
	1) Insertion using 
		i) append()
		ii) insert()

	2) Deletion using
		i) pop()
		ii) remove

	3) Return Index using index()

	4) Reverse the array using reverse()
	-----------------------------------------------

'''

import array as arr 

list1 = [] # this is simple list
arr = arr.array('i',list1)

# first funtion : print the array
def print_array(arr) :
	print('================================================')
	print('Current array elements are :',end=' ')
	for i in arr :
		print(i,end=' ')

	# Calling execute_all()
	execute_all(arr)

# This second function will append the element to the last of array (append())
def append_element(arr,element) :
	# append()
	arr.append(element)
	print('Element appended successfully !')
	print_array(arr)

# This third function will insert element at certain index (insert())
def insert_at_index(arr,index,element) :
	# insert()
	arr.insert(index,element)
	print('Element inserted at ',index)
	print_array(arr)

# Delete the element at specific index (pop())
def delete_at_index(arr,index) :
	if len(arr) == 0 :
		print('Array is empty !! add some elements')
	else :
		print(arr[index],' was popped !')

		# pop()
		arr.pop(index)
		print_array(arr)

# Delete the first occurence of the value provided (remove())
def remove_element(arr,element) :
	if len(arr) == 0 :
		print('Array is empty !! add some elements')
	else :
		print(element,' was deleted !!')

		# remove()
		arr.remove(element)
		print_array(arr)

# This function will give the index of the first occurence of element (index())
def return_index(arr,element) :
	if len(arr) == 0 :
		print('Array is empty !! add some elements')
	else :
		# index()
		print('The index of ',element,' is ',arr.index(element))
		print_array(arr)
	

# This last function will reverse the array (reverse())
def reverse_arr(arr) :
	if len(arr) == 0 :
		print('Array is empty !! add some elements')
	else :
		# reverse()
		arr.reverse()
		print('Reversed array elements are :',end=' ')
		for i in arr :
			print(i,end=' ')

		# Calling execute_all()
		execute_all(arr)
	

'''
This function is main function , it will let user decide what to do with the array !!
'''
def execute_all(arr) :
	print('\n================================================')
	print('Choose the actions below !')
	print('1. append')
	print('2. insert')
	print('3. pop')
	print('4. remove')
	print('5. index')
	print('6. reverse')
	print('7. show the array elements')
	print('8. Quit')
	print('================================================')


	choice = int(input('whats your choice ? ==> '))
	if choice == 1 :
		element = int(input('Enter the element you wanted to insert ! ==> '))
		append_element(arr,element)
	elif choice == 2 :
		index = int(input('Enter the index at which you wanted to insert the element ! ==> '))
		element = int(input('Enter the element ! ==> '))
		insert_at_index(arr,index,element)
	elif choice == 3 :
		index = int(input('Enter the index ! ==> '))
		delete_at_index(arr,index)
	elif choice == 4:
		element = int(input('Enter the element ! ==> '))
		remove_element(arr,element)
	elif choice == 5 :
		element = int(input('Enter the element ! ==> '))
		return_index(arr,element)
	elif choice == 6 :
		reverse_arr(arr)
	elif choice == 7 :
		print_array(arr)
	elif choice == 8 :
		pass
	else :
		print('Wrong input ! please try again')
		execute_all(arr)

# Calling execute all	
execute_all(arr)