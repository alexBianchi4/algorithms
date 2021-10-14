'''
Merge Sort
Overview:
    - sorts a list in ascending order
    - Good for lists with a large amount of numbers of any range
    - reliable becuase it's run time is always the same (best case = worse case)
    - preffered for sorting linked lists
Time Complexity:
    always O(nlogn)
How it works:
    -recursively splits a list in half and sorts each half, once each half is sorted they are passed to the merge function
    to combine them into one list
'''
def mergesort(arr):
    if len(arr) < 2:
       return arr 
    middle = len(arr)//2
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])
    return merge(left,right)

def merge(left,right):
    sorted=[]
    i=j=0
    length = len(left) + len(right)
    for k in range(length):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
        
        if i==len(left):
            sorted.extend(right[j:])
            break;
        elif j==len(right):
            sorted.extend(left[i:])
            break;
  
    return sorted