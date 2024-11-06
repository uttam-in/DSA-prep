def binarysearchIter(arr, key):
    index = -1
    low = 0 
    high = len(arr) -1
    mid = None
    while(low <= high):
        mid = low + ((high-low)//2)
        if arr[mid] == key:
            index = mid
            break
        elif arr[mid] < key:
            low = mid + 1
            pass
        else:
            high = mid -1
        
    return index

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = binarysearchIter(arr, 10)

print(index)

# TC = O(log(N))
# SC = O(1)

# Why Use <= Instead of <:
# Single Element Check: When low equals high, the subarray contains a single element. 
# It's essential to check this element to determine if it matches the target value.
# Termination Condition: If the target value is not found, the loop will eventually adjust 
# low to be greater than high (low > high), at which point the loop terminates, indicating 
# that the target is not present in the array.