'''
	-----------------------------------------------------------------
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (Insertion Sort Algorithm)
	-----------------------------------------------------------------
'''
def selection_sort(array, size) :
	'''
		Algo :
			InsertionSort(array) 
				Mark first element as sorted
				for each unsorted element X
					"extract" the element X 
						for j <- lastSortedElement down to 0 
							if current j > X
								move sorted element to right by 1
						break loop and insert X here 
			end SelectionSort
	'''
	for step in range(1,len(array)) :
		selected = array[step]
		j = step - 1

		while j >= 0 and selected < array[j] :
			array[j+1] = array[j]
			j = j-1

		array[j+1] = selected


# Driver Code 
example = [88,62,3,-1,-99,62,8,-77,0]
print('Array before sorting\n',example)
selection_sort(example,len(example))
print('Array after sorting\n',example)
# Output should be [-99, -77, -1, 0, 3, 8, 62, 62, 88]   