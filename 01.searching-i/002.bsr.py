def binarysearchRec(arr, key, low, high):    
    index = -1
    # Base case: If the range is invalid, key is not in the array
    if low > high:
        return -1
        
    mid = low + ((high-low)//2)
    
    if key == arr[mid]:
        index = mid
        return index
    
    if arr[mid] < key:
        index = binarysearchRec(arr, key, mid+1, high)
    else:
        index = binarysearchRec(arr, key, low, mid-1)
        
    return index

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = binarysearchRec(arr, 8, 0, len(arr)-1)

print(index)