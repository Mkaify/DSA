class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binary strings and returns their sum as a binary string.
        
        VocloneTranslate Analogy:
        Simulates a hardware Full Adder circuit, mimicking the exact bit-level 
        summation used during low-level digital signal mixing of vocal tracks.
        
        Time Complexity: O(max(N, M)) - Single pass through the longer string.
        Space Complexity: O(max(N, M)) - To store the resulting characters.
        """
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        # Sloop until both binary streams are exhausted and no carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            # Extract and add bit from string 'a'
            if i >= 0:
                total += int(a[i])
                i -= 1
                
            # Extract and add bit from string 'b'
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # The current column's output bit is total modulo 2
            result.append(str(total % 2))
            
            # The new carry value is the integer division of total by 2
            carry = total // 2
            
        # Reverse the accumulated bits to restore the correct order
        return "".join(reversed(result))

# --- Test Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Executing directly with parameters (no print statements, as per instructions)
    sol.addBinary("11", "1")
    sol.addBinary("1010", "1011")
    sol.addBinary("0", "0")