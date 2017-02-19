"""
mergeSort
quickSort
selectionSort

"""





'''
Created on Feb 18, 2017

@author: fanxueyi
'''
def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)
    return(arr)        
        

def partition(arr, low, high):
    pivot = arr[low]
    i = low +1
    for j in range(low+1, high+1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i-1] = arr[i-1], arr[low]
    return(i-1)


def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = arr[0]
        index = 0
        for j in range(0, n-i):
            if arr[j] < min:
                min = arr[j]
                index = j
        arr[index], arr[-1-i] = arr[-1-i], arr[index]
    return(arr)


def mergeSort(arr):
    if len(arr) ==1:
        return(arr)
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return(mergeOrdered(left, right))
    

def mergeOrdered(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i, j = 0, 0
    output = []
    while i< n1 or j < n2:
        if i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                output.append(arr1[i])
                i +=1
            else:
                output.append(arr2[j])
                j += 1
        if i >= n1:
            output += arr2[j:]
            return(output)
        if j >= n2:
            output += arr1[i:]
            return(output)
    

print(mergeSort([3,2,1,5,2,4]))
print(mergeOrdered([1,3,4], [2,3,5]))

print(selectionSort([3,1,2,5,6,1]))
print(quicksort([0], 0, 0))
print(quicksort([3,1,2,5,6,1], 0, 5))