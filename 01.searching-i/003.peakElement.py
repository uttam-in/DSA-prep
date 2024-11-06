class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        low = 0
        high = len(A) - 1
        
        while low <= high:
            mid = low + (high - low) // 2

            # Check if mid is a peak element
            if (mid == 0 or A[mid] >= A[mid - 1]) and (mid == len(A) - 1 or A[mid] >= A[mid + 1]):
                return A[mid]

            # Move to the side where the peak element exists
            if mid > 0 and A[mid] < A[mid - 1]:
                high = mid - 1  # Peak is on the left side
            else:
                low = mid + 1   # Peak is on the right side

        return -1
                
        
sol = Solution()

input = [1, 2, 3, 4, 5]
print(sol.solve(input))