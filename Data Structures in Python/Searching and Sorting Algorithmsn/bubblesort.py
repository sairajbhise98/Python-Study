'''
	-------------------------------------------------------------
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (Bubble Sort Algorithm)
	-------------------------------------------------------------
'''

def bubble_sort(array) :
	'''
		Algo :
		for i <- 0 to indexOfLastElement - 1 
			if leftElement > rightElement 
				swap(leftElement,rightElement)
	'''

	for i in range(len(array)) :
		for j in range(len(array) - i - 1) :
			if array[j]  > array[j+1] :	
				(array[j],array[j+1]) = (array[j+1],array[j])
				



# Heres the driver code
example = [88,62,3,-1,-99,62,8,-77,0]
print('Array before sorting\n',example)
bubble_sort(example)
print('Array after sorting\n',example)
# Output should be [-99, -77, -1, 0, 3, 8, 62, 62, 88]   