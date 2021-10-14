'''
Counting Sort
Overview:
    - linear time sorting algorithm (only works with numeric keys) 
    - stable sorting
    - works the best when the range of numbers a value can be is small, for example all elements are less than 10
Time Complexity:
    O(n+k)
How it works:
    - works on the assumption that numbers to be sorted are in range {0,1,...,k} and numbers are greater than 0
    - Creates a list of zeros C, the size of the max element in A
    - For i=0 to i=len(A), add 1 to C[A[i]] to count the occurence of each number in A
    - Then in C add each number accumatively, for example
        [1,2,4,0,3] --becomes--> [1,1+2.1+2+4,1+2+4+0,1+2+4+0+3] ---> [1,3,7,7,10]
    - Then shift the array to the right by one so from the above example our array becomes [0,1,3,7,7]
    - These numbers are now the starting indecies for the range of numbers in our array C
    - Now we increment through A and for all i in A we get the index we should place i in from C[i]
    - Once we place i we increment C[i] and continue unti all elements are placed
'''

def countingsort(A):
    return countsort(A,max(A))

def countsort(A,k):
    ans = A.copy() #our sorted list
    C = [0 for i in range(k+1)] #the list for storing counts
    for i in A:
        C[i]+=1
    #C[i] now contains the number of elements equal to i
    
    for i in range(1,len(C)):
        C[i] += C[i-1]
    #C[i] now contains the number of elements less than or equal to i

    for i in range(len(C)-1,0,-1):
        C[i]=C[i-1]
    C[0]=0
    #shift the values in C

    for i in range(len(A)):
        ans[C[A[i]]] = A[i]
        C[A[i]] +=1 
    
    return ans