import math
from insertionsort import insertionsort
'''
Bucket Sort
Overview:
    - stable sort
    - really good for sorting lists with a uniform random distribution
      but not for something that follows for example a bell curve like grades
Time Complexity:
    worst case (all items in one bucket): O(n^2)
    Average case (uniform random distrubution): O(n)
How it works:
    - you create a list of lists(buckets) that has as many buckets as the list being sorted has elements
    - then you divide the list up into these buckets based on their value and use insertion sort on each individual bucket
    - this makes it so each bucket is sorted and since the numbers were divided into buckets based on their size/value 
      all the buckets are sorted in respect to eachother already
    - then you just empty all of the buckets into one list and you have your answer
'''

def bucketsort(A):
    size=len(A)
    maxVal=max(A)
    buckets = [[] for i in range(size+1)]
    for i in A:
        buckets[math.floor(size*(i/maxVal))].append(i)
    for bucket in buckets:
        insertionsort(bucket)
    
    A=[]
    for bucket in buckets:
        while len(bucket) != 0:
            A.append(bucket.pop(0))
    return A