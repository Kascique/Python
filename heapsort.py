def swap(i, j):                    
    num_array[i], num_array[j] = num_array[j], num_array[i] 

def heapify(end,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and num_array[i] < num_array[l]:   
        max = l   
    if r < end and num_array[max] < num_array[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   

def heap_sort():     
    end = len(num_array)   
    start = end 
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        swap(i, 0)   
        heapify(i, 0)   

num_array = [3, 7, -1, 4, 5, -8, 10, 23, 70]
heap_sort()
print(num_array)
