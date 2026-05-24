class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Divides two integers using bit manipulation and subtraction.
        
        Time Complexity: O(log^2 N)
        Space Complexity: O(1)
        """
        # Constants for 32-bit signed integer limits
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        # Special case: Overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        # If signs are different, result is negative
        is_negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        a, b = abs(dividend), abs(divisor)
        quotient = 0

        # Main loop: Subtract chunks from the dividend
        while a >= b:
            temp_divisor = b
            count = 1
            # Double the divisor and count until it exceeds the current dividend
            # (temp_divisor << 1) is equivalent to temp_divisor * 2
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1
            
            # Subtract the largest chunk found and add its count to quotient
            a -= temp_divisor
            quotient += count

        # Apply the sign and ensure the result is within 32-bit bounds
        result = -quotient if is_negative else quotient
        return max(MIN_INT, min(MAX_INT, result))

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: 10 / 3 -> 3
    sol.divide(10, 3)
    
    # Example 2: 7 / -3 -> -2
    sol.divide(7, -3)
    
    # Boundary Test: MIN_INT / -1 -> MAX_INT
    sol.divide(-2147483648, -1)