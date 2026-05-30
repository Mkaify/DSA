class Solution:
    def binaryDateConverter(self, date: str) -> str:
        """
        Converts a yyyy-mm-dd date string into its binary representation.
        
        Time Complexity: O(1) - The date format is fixed length, and binary conversion 
                         of small integers (up to 2100) is constant time.
        Space Complexity: O(1) - Fixed number of string operations.
        """
        # Step 1: Split the date into year, month, and day parts
        # "2080-02-29" -> ["2080", "02", "29"]
        parts = date.split("-")
        
        # Step 2: Convert each part to an integer and then to a binary string
        # bin(x) returns a string like '0b101', so we slice from index 2 to remove '0b'
        binary_parts = []
        for part in parts:
            # int(part) handles leading zeros automatically (e.g., "02" -> 2)
            binary_val = bin(int(part))[2:]
            binary_parts.append(binary_val)
            
        # Step 3: Join the binary strings back with hyphens
        return "-".join(binary_parts)

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: 2080-02-29
    # 2080 -> 100000100000
    # 02   -> 10
    # 29   -> 11101
    sol.binaryDateConverter('2080-02-29')
    
    # Example 2: 1900-01-01
    # 1900 -> 11101101100
    # 01   -> 1
    # 01   -> 1
    sol.binaryDateConverter('1900-01-01')