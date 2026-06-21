from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """
        Determines if each value in the array occurs a unique number of times.
        
        Time Complexity: O(n) - We iterate through the array to count, then 
                         iterate through the unique values to check counts.
        Space Complexity: O(n) - To store the counts and the set of counts.
        """
        # Step 1: Count the frequency of each number in the array
        # Example: [4, 5, 5, 4, 4, 6] -> {4: 3, 5: 2, 6: 1}
        counts = Counter(arr)
        
        # Step 2: Extract all the frequency values
        # Example: [3, 2, 1]
        occurrences = list(counts.values())
        
        # Step 3: Check if the number of unique counts equals the total number of counts
        # A set only stores unique elements. If its length matches the original list,
        # all counts were unique.
        return len(occurrences) == len(set(occurrences))

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: [4, 5, 5, 4, 4, 6]
    # Counts: 4 -> 3 times, 5 -> 2 times, 6 -> 1 time.
    # Frequencies: [3, 2, 1]. All unique.
    sol.uniqueOccurrences([4, 5, 5, 4, 4, 6]) # Expected: True
    
    # Example 2: [2, 3]
    # Counts: 2 -> 1 time, 3 -> 1 time.
    # Frequencies: [1, 1]. Not unique.
    sol.uniqueOccurrences([2, 3]) # Expected: False
    
    # Example 3: [-2, 0, 2, -2, 2, 2, 2, -2, 11, 0]
    # Counts: -2 -> 3, 0 -> 2, 2 -> 4, 11 -> 1.
    # Frequencies: [3, 2, 4, 1]. All unique.
    sol.uniqueOccurrences([-2, 0, 2, -2, 2, 2, 2, -2, 11, 0]) # Expected: True