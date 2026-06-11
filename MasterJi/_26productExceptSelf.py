class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Calculates the product of all elements except nums[i] without division.
        
        Algorithm:
        1. Create a result array where each index i stores the product of all elements to its left.
        2. Iterate backwards to multiply each index by the product of all elements to its right.
        
        Time Complexity: O(n)
        Space Complexity: O(1) (excluding the output array)
        """
        n = len(nums)
        if n == 0:
            return []
            
        # Initialize output array
        res = [1] * n
        
        # Pass 1: Prefix Products
        # After this loop, res[i] contains the product of everything from nums[0] to nums[i-1]
        left_running_product = 1
        for i in range(n):
            res[i] = left_running_product
            left_running_product *= nums[i]
            
        # Pass 2: Suffix Products
        # We multiply the current res[i] (which is the prefix) by the suffix product
        right_running_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_running_product
            right_running_product *= nums[i]
            
        return res

# --- Verification ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: [1, 2, 3, 4]
    # Prefix: [1, 1, 2, 6]
    # Suffix multiplication:
    # i=3: 6 * 1 = 6
    # i=2: 2 * 4 = 8
    # i=1: 1 * 12 = 12
    # i=0: 1 * 24 = 24
    # Expected: [24, 12, 8, 6]
    sol.productExceptSelf([1, 2, 3, 4])
    
    # Test Case 2: [-1, 1, 0, -3, 3]
    # Expected: [0, 0, 9, 0, 0]
    sol.productExceptSelf([-1, 1, 0, -3, 3])