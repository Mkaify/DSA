class Solution:
    def checkForDuplicates(self, nums: list[int]) -> bool:
        """
        Determines if any value appears at least twice in the array.
        
        Time Complexity: O(n) - Set construction takes linear time.
        Space Complexity: O(n) - To store elements in the set.
        """
        # A more efficient and Pythonic way to check for duplicates:
        # If the length of the set (unique elements) is less than the 
        # length of the original list, there must be duplicates.
        return len(set(nums)) != len(nums)

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # We use .lower() to match the 'true'/'false' format expected by some judges
    
    # Example 1: [2, 5, 6, 2] -> True (2 is repeated)
    str(sol.checkForDuplicates([2, 5, 6, 2])).lower()
    
    # Example 2: [4, 7, 9, 1] -> False (All distinct)
    str(sol.checkForDuplicates([4, 7, 9, 1])).lower()
    
    # Example 3: [8, 8, 8, 5, 5, 7, 5, 3, 7, 3] -> True
    str(sol.checkForDuplicates([8, 8, 8, 5, 5, 7, 5, 3, 7, 3])).lower()