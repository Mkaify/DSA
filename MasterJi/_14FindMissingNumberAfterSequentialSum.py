class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        """
        Finds the sum of the longest sequential prefix and returns the 
        smallest missing integer >= that sum.
        
        Time Complexity: O(n) - One pass to sum the prefix, one to check missing.
        Space Complexity: O(n) - To store the nums in a set for O(1) lookup.
        """
        # Step 1: Find the sum of the longest sequential prefix
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            # Check if current number is exactly 1 greater than the previous
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                # Sequence broken
                break
        
        # Step 2: Convert nums to a set for O(1) lookup performance
        num_set = set(nums)
        
        # Step 3: Find the smallest missing integer >= prefix_sum
        current_val = prefix_sum
        while current_val in num_set:
            current_val += 1
            
        return current_val

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: nums = [2,3,4,3,6]
    # Prefix: [2,3,4] -> Sum: 9
    # Is 9 in [2,3,4,3,6]? No.
    # Output: 9
    sol.missingInteger([2,3,4,3,6])

    # Example 2: nums = [1,2,3,2,5]
    # Prefix: [1,2,3] -> Sum: 6
    # Is 6 in [1,2,3,2,5]? No.
    # Output: 6
    sol.missingInteger([1,2,3,2,5])

    # Example 3: nums = [4,5,6,2,10,15,16]
    # Prefix: [4,5,6] -> Sum: 15
    # Is 15 in array? Yes. -> 16
    # Is 16 in array? Yes. -> 17
    # Is 17 in array? No.
    # Output: 17
    sol.missingInteger([4,5,6,2,10,15,16])