class Solution:
    def evaluateExpression(self, s: str) -> int:
        """
        Evaluates a basic arithmetic expression with +, -, and ().
        
        Time Complexity: O(n) - Single pass through the string.
        Space Complexity: O(n) - In the worst case, the stack stores nested results.
        """
        stack = []
        current_result = 0
        current_sign = 1  # 1 for '+', -1 for '-'
        i = 0
        n = len(s)
        
        while i < n:
            char = s[i]
            
            if char.isdigit():
                # Form the full number from consecutive digits
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                # Apply the sign and add to running total
                current_result += current_sign * num
                # Adjust index back because the outer loop will increment it
                i -= 1
                
            elif char == '+':
                current_sign = 1
                
            elif char == '-':
                current_sign = -1
                
            elif char == '(':
                # Push current result and sign to save context for the sub-expression
                stack.append(current_result)
                stack.append(current_sign)
                # Reset result and sign for inner parentheses
                current_result = 0
                current_sign = 1
                
            elif char == ')':
                # Sub-expression is finished. Pop the sign first, then the previous result.
                prev_sign = stack.pop()
                prev_result = stack.pop()
                # Update current_result: result_of_sub_expression * sign_before_parens + previous_total
                current_result = prev_result + (prev_sign * current_result)
            
            # Spaces are skipped automatically by doing nothing
            i += 1
            
        return current_result

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: "1 + 1" -> 2
    sol.evaluateExpression("1 + 1")
    
    # Example 2: " 2-1 + 2 " -> 3
    sol.evaluateExpression(" 2-1 + 2 ")
    
    # Example 3: "(1+(4+5+2)-3)+(6+8)" -> 23
    sol.evaluateExpression("(1+(4+5+2)-3)+(6+8)")