'''
	-------------------------------------------------------------
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (Optimised Bubble Sort Algorithm)
	-------------------------------------------------------------
'''

def bubble_sort(array) :
	'''
		Algo :
		swapped = false
		for i <- 0 to indexOfLastElement - 1 
			if leftElement > rightElement 
				swap(leftElement,rightElement)
				swapped = true
		if !swapped 
			stop
	'''
	for i in range(len(array)) :
		# initialise swapped to false every loop
		swapped = False
		for j in range(len(array) - i - 1) :
			if array[j]  > array[j+1] :	
				(array[j],array[j+1]) = (array[j+1],array[j])
				swapped = True # update swapped
		'''
		if swapping is not taking place 
		'''
		if !swapped :
			break
				



# Heres the driver code
example = [88,62,3,-1,-99,62,8,-77,0]
print('Array before sorting\n',example)
bubble_sort(example)
print('Array after sorting\n',example)
# Output should be [-99, -77, -1, 0, 3, 8, 62, 62, 88]   