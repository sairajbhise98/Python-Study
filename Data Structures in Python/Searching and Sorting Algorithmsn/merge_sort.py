'''
    -----------------------------------------------------------------
    Code By : Sairaj Bhise
    Topic : Data Structures and Algorithms (Merge Sort Algorithm)
    -----------------------------------------------------------------
'''

'''
Algo :
    MergeSort(Array, start, end):
        if start > end 
            return
        middle = (start+end)/2
        mergeSort(Array, start, middle)
        mergeSort(Array, middle+1, end)
        merge(Array, start, middle, end)
'''

def merge_sort(array) :
    if len(array) > 1 :
        middle = len(array)//2
        L = array[:middle]
        M = array[middle:]
        merge_sort(L)
        merge_sort(M)
        
        i = j = k = 0 
        while i<len(L) and j<len(M) :
            if L[i] < M[j] :
                array[k] = L[i]
                i += 1
            else :
                array[k] = M[j]
                j += 1
            k += 1
            
        while i < len(L) :
            array[k] = L[i]
            i += 1
            k += 1
        
        while j < len(M) :
            array[k] = M[j]
            j += 1
            k += 1

#Driver Code
example = [88,62,3,-1,-99,62,8,-77,0]
print('Array before sorting\n',example)
merge_sort(example)
print('Array after sorting\n',example)
# Output should be [-99, -77, -1, 0, 3, 8, 62, 62, 88]   
