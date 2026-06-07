class Solution:
    def isOneBitCharacter(self, bits):
        '''
        bits: List[int] - array of integers representing the bits (0s and 1s)
        '''
        # Your implementation here
        
        i = 0
        n = len(bits)
        
        # Traverse until we are just before the last bit
        while i < n - 1:
            if bits[i] == 1:
                # Must be a 2-bit character (10 or 11)
                i += 2
            else:
                # Must be a 1-bit character (0)
                i += 1
        
        # If the pointer is at n-1, it means we landed exactly on the last bit.
        # This implies the last bit is a standalone 1-bit character.
        # If i is n, it means a 2-bit character consumed the last bit.
        return i == n - 1

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: [1, 0, 0]
    # i=0 (1) -> i=2. Loop ends. i=2 is the last index. Result: True.
    sol.isOneBitCharacter([1, 0, 0])
    
    # Example 2: [1, 1, 1, 0]
    # i=0 (1) -> i=2. i=2 (1) -> i=4. Loop ends. i=4 != 3. Result: False.
    sol.isOneBitCharacter([1, 1, 1, 0])
    
    # Example 3: [0]
    # Loop doesn't run. i=0 is the last index. Result: True.
    sol.isOneBitCharacter([0])
