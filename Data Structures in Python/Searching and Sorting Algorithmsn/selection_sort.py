'''
	-----------------------------------------------------------------
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (Selection Sort Algorithm)
	-----------------------------------------------------------------
'''
def selection_sort(array, size) :
	'''
		Algo :
			SelectionSort(array,size) 
				repeat (size-1) times
				set the first element as the minimum
					for each unsorted array 
						if current_minimum > element 
							set the element as new minimum
					swap the minimum with the first element of unsorted list
			end SelectionSort
	'''
	for step in range(size-1) :
		min_ind = step 
		for i in range(step+1,size) :
			if array[min_ind] > array[i] :
				min_ind = i
		(array[step],array[min_ind]) = (array[min_ind],array[step])


# Driver Code 
example = [88,62,3,-1,-99,62,8,-77,0]
print('Array before sorting\n',example)
selection_sort(example,len(example))
print('Array after sorting\n',example)
# Output should be [-99, -77, -1, 0, 3, 8, 62, 62, 88]   