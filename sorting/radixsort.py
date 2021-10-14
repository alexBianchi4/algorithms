'''
Radix Sort
Overview:
    - linear time sorting algorithm (only works with numeric keys) 
    - stable sorting
Time Complexity:
    O(d(n+k))
How it works:
    - views each number as a multi-digit string
    - uses count sort to sort by least significant digit to the most significant
'''

 #call this function
def radixSort(A):
    d = 0
    val = max(A)
    while val > 0:
        val= val//10
        d+=1
    return rsort(A,d)

def rsort(A,d):
    for i in range(1,d+1):
        A = countsort(A,i,d)
    return A


#see countingsort.py for my explanation of how counting sort works
#this is a modified version that handles index of the number
def countsort(A,i,d):
    ans = A.copy() #our sorted list
    B = []
    C = [0 for i in range(10)] #the list for storing counts
    for j in A:
        strNum = str(j)
        strNum = strNum.zfill(d)
        B.append(strNum)
        C[int(strNum[-i])]+=1

    for j in range(1,len(C)):
        C[j] += C[j-1]

    for j in range(len(C)-1,0,-1):
        C[j]=C[j-1]
    C[0]=0

    for j in range(len(A)):
        ans[C[int(B[j][-i])]] = A[j]
        C[int(B[j][-i])] +=1 
    return ans