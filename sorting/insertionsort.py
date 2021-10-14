'''
Insertion Sort
overview:
    - stable sort, in-place
    - useful when the list we are sorting is very small
    - useful if the list is mostly sorted already
Time Complexity:
    O(n^2)
How it Works:
    - works like ordering a hand of playing cards
    - starting from the second item in the list you compare it to the items before it,
      if it is smaller you move it to the left of the item you compared it to and so on 
      until you find a spot where it is greater than the item before it or it is now the first item in the list
'''

def insertionsort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j > -1 and key < A[j]:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key