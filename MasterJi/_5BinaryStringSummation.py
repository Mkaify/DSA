class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binary strings and returns the result as a binary string.
        
        Time Complexity: O(max(N, M)) where N and M are lengths of strings a and b.
        Space Complexity: O(max(N, M)) to store the result.
        """
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        # Loop until both strings are exhausted and no carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # If total is 0 or 2, bit is 0. If 1 or 3, bit is 1.
            result.append(str(total % 2))
            
            # If total is 2 or 3, carry becomes 1. Otherwise 0.
            carry = total // 2
            
        # The result list is built backwards, so reverse it
        return "".join(reversed(result))

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    # 1101 + 101 = 10010
    sol.addBinary('1101', '101')
    
    # Example 2
    # 1010 + 1011 = 10101
    sol.addBinary('1010', '1011')
    
    # Example 3 (Carry at the end)
    # 1 + 1 = 10
    sol.addBinary('1', '1')