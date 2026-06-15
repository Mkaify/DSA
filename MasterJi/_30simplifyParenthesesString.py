class Solution:
    def simplifyParentheses(self, s: str) -> str:        
        result = []
        depth = 0
        
        for char in s:
            if char == '(':
                # If depth > 0, this '(' is not an outermost parenthesis
                if depth > 0:
                    result.append(char)
                depth += 1
            elif char == ')':
                depth -= 1
                # If depth > 0 after decrementing, this ')' is not an outermost parenthesis
                if depth > 0:
                    result.append(char)
                    
        return "".join(result)

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: "(()())(())" -> "()()()"
    # Decomposition: "(()())" + "(())" -> "()()" + "()"
    sol.simplifyParentheses('(()())(())')
    
    # Example 2: "(()())(())(()(()))" -> "()()()()(())"
    sol.simplifyParentheses('(()())(())(()(()))')
    
    # Example 3: "()()" -> ""
    # Decomposition: "()" + "()" -> "" + ""
    sol.simplifyParentheses('()()')