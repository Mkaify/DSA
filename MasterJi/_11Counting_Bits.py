class Solution:
    def countBits(self, n: int) -> list[int]:
        """
        Calculates the number of 1s in the binary representation for each 
        number from 0 to n using Dynamic Programming.
        
        Time Complexity: O(n) - We iterate through the numbers once.
        Space Complexity: O(n) - To store the result array.
        """
        # Initialize the result array with 0s
        ans = [0] * (n + 1)
        
        # We start from 1 because ans[0] is already 0
        for i in range(1, n + 1):
            # i >> 1 is the same as i // 2
            # i & 1 is 1 if odd, 0 if even
            # We use the previously calculated value of i/2 and add the last bit
            ans[i] = ans[i >> 1] + (i & 1)
            
        return ans

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: n = 2
    # 0 -> 00 (0), 1 -> 01 (1), 2 -> 10 (1)
    # Output: [0, 1, 1]
    sol.countBits(2)
    
    # Example 2: n = 5
    # 0 -> 0, 1 -> 1, 2 -> 1, 3 -> 2, 4 -> 1, 5 -> 2
    # Output: [0, 1, 1, 2, 1, 2]
    sol.countBits(5)
    
    # Example 3: n = 0
    sol.countBits(0)