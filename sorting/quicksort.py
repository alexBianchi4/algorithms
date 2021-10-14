'''
Quick Sort
Overview:
    - Sorts a list in ascending order
    - Similar performance to merge sort but not as good in all situations,
      the benefit is that it is an in place algorithm, meaning that it takes no extra space besides the recursion stack
    - good for sorting arrays
Time complexity:
    Worst case: already sorted/lots of repeating digts --> O(n^2) 
    Best case: The pivot is at the end of the list --> O(nlogn)
    Average case: O(nlogn) based on the list being ordered randomly without lots of duplicates
How it works:
    quicksort sorts it's elements around a pivot, in this implementation we pick our pivot to be the last element in the list.
    we compare all the values of the list to the pivot and move them to the left of the pivot if they are less than it,
    and to the right if they are greater. the ordering of the numbers do not matter all that matters is they are less than or greateer.
    We then recursively call quicksort on the elements to either side of the pivot
    as the pivot is guaranteed to remain in place after the other elements have been sorted around it.
    We do this until all the elements are in the proper place.
'''

'''helper function'''
def quicksort(A):
    qs(A,0,len(A)-1)

'''takes a list A and sorts it between the bounds of l and r'''
def qs(A,l,r):
    if l >= r: #section of our array has one or zero elements, already sorted
        return
    pivot = partition(A,l,r) # find the index of the pivot
    #recursively sort the elements to the left and right of the pivot
    qs(A,l,pivot-1)
    qs(A,pivot+1,r)

'''
partitions a section of a list between l & r
to partition we need to choose a pivot, we will take the last element as our pivot
the goal of the function is to divide the list into two groups,
one group that has the elements less than the pivot and one group with elements greater than the pivot
the pivot will be inbetween the two groups of numbers
we do not care about the ordering of the numbers in the two groups
this function returns the new index of the pivot
'''
def partition(A,l,r):
    #set our pivot to the last element in the range
    pivot=A[r]
    #all the numbers up to i are less than the pivot, numbers between i and j are greater than the pivot
    i=l-1
    for j in range(l,r):
        if A[j] < pivot:
            i+=1
            A[i],A[j]=A[j],A[i] #swap the values of A[i] and A[j]
    A[i+1],A[r] = A[r],A[i+1] #swap the pivot with A[i+1]
    return i+1 #this is the index of the pivot