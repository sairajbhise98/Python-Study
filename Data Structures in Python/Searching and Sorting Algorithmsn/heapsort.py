'''
	-------------------------------------------------------------
	Code By : Sairaj Bhise
	Topic : Data Structures and Algorithms (Heap Sort Algorithm)
	-------------------------------------------------------------
'''
def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
  
  
def heapSort(arr):
    n = len(arr)
  
    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
  
        # Heapify root element
        heapify(arr, i, 0)


# Heres the driver code
example = [88,62,3,-1,-99,62,8,-77,0]
print('Array before sorting\n',example)
heapSort(example)
print('Array after sorting\n',example)
# Output should be [-99, -77, -1, 0, 3, 8, 62, 62, 88]   