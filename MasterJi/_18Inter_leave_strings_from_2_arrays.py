class Solution:
    def interleaveArrays(self, first_list: list[str], second_list: list[str]) -> list[str]:
        """
        Interleaves two lists of strings, starting with the first list.
        Remaining elements of the longer list are appended to the result.
        
        Time Complexity: O(N + M) where N and M are the lengths of the lists.
        Space Complexity: O(N + M) to store the result.
        """
        result = []
        n1, n2 = len(first_list), len(second_list)
        
        # Iterate through both lists up to the point where one runs out
        i = 0
        while i < n1 and i < n2:
            result.append(first_list[i])
            result.append(second_list[i])
            i += 1
            
        # Append remaining elements from first_list if any
        if i < n1:
            result.extend(first_list[i:])
            
        # Append remaining elements from second_list if any
        if i < n2:
            result.extend(second_list[i:])
            
        return result

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: Equal lengths
    # Input: ["x", "y"], ["1", "2"] -> ["x", "1", "y", "2"]
    sol.interleaveArrays(['x', 'y'], ['1', '2'])
    
    # Example 2: First list is longer
    # Input: ["a", "b", "c"], ["1"] -> ["a", "1", "b", "c"]
    sol.interleaveArrays(['a', 'b', 'c'], ['1'])
    
    # Example 3: Second list is longer
    # Input: ["a"], ["1", "2", "3"] -> ["a", "1", "2", "3"]
    sol.interleaveArrays(['a'], ['1', '2', '3'])