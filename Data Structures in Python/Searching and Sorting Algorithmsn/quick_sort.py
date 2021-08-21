'''
    -----------------------------------------------------------------
    Code By : Sairaj Bhise
    Topic : Data Structures and Algorithms (Quick Sort Algorithm)
    -----------------------------------------------------------------
'''

def quick_sort(array,low,high) :
    '''
    Algo :
        QuickSort(array,low,high) 
            if low < high
            pi <- partition(array,low,high)
            QuickSort(array,low,pi-1)
            QuickSort(array,pi+1,high)
    '''
    if low < high :
        pi = partition(array,low,high)
        quick_sort(array,low,pi-1)
        quick_sort(array,pi+1,high)
        
def partition(array,low,high) :
    '''
    Algo :
        Partition(Array,low,high)
            pivot <- array[high]
            IndexOfSmallerNumber <- low-1
            for j from low to high
                if array[j] < pivot
                    i++
                    swap(array[i],array[j])
            swap(array[i+1],array[high])
            return IndexOfSmallerNumber+1
    '''
    pivot = array[high] 
    i = low-1
    for j in range(low,high):
        if array[j] < pivot :
            i += 1
            (array[i],array[j]) = (array[j],array[i])
    (array[i+1],array[high]) = (array[high],array[i+1])
    return i+1

#Driver Code
example = [11,1,2,3,4,5,6,7,8,10]
print('Array before sorting\n',example)
quick_sort(example,0,len(example)-1)
print('Array after sorting\n',example)
# Output should be [-99, -77, -1, 0, 3, 8, 62, 62, 88]   