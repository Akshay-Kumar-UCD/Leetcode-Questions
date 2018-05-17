# MergeSort Algorithm implemented 
""" The following function sorts a given linked list in sections, based on the l, m, and r arguments. """
def MergeSort(arr,l,m,r):
    # find lengths of two halves
    lenL = m - l + 1
    lenR = r - m
    # create temporary arrays to store the halves' values
    L = [0] * lenL
    R = [0] * lenR
    # store the halves' values in the temporary arrays
    for i in range(lenL):
        L[i] = arr[l+i]
    for j in range(lenR):
        R[j] = arr[m+1+j]
    # now we rewrite the linked list's contents by sorting values from the temporary arrays
    i,j = 0,0
    k = l
    while i < lenL and j < lenR:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < lenL:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < lenR:
        arr[k] = R[j]
        j += 1
        k += 1

""" The following function splits a given linked list into halves, until each half is only one element in size. """
def Halve(arr,l,r):
    # stops running when the linked list has been traveled through
    if l < r:
        # finds halfway index
        m = int((l + (r - 1)) / 2)
        # halve left half, then right half, then merge till the list is completely sorted
        Halve(arr,l,m)
        Halve(arr,m+1,r)
        MergeSort(arr,l,m,r)
    

test_list = [2,1,5,3,9]
print("Before: ",test_list)
Halve(test_list,0,len(test_list)-1)
print("After: ",test_list)
