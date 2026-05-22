class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        moves_needed = 0
        balance = 0
        
        for char in s:
            if char == '(':
                # We have an open bracket waiting for a match
                balance += 1
            else:
                # We have a closing bracket
                if balance > 0:
                    # Match it with an existing open bracket
                    balance -= 1
                else:
                    # No open bracket available, we must insert one
                    moves_needed += 1
        
        # After the loop, 'balance' represents open brackets that never found a match.
        # We must add closing brackets for all of them.
        return moves_needed + balance


if __name__ == "__main__":
    
    sol= Solution()
    # Example 1: "())" -> Needs 1 '(' at the start. Result: 1
    sol.minAddToMakeValid("())")
    
    # Example 2: "(((" -> Needs 3 ')' at the end. Result: 3
    sol.minAddToMakeValid("(((")
    
    # Example 3: "()" -> Already valid. Result: 0
    sol.minAddToMakeValid("()")
    
    # Example 4: "()))((" -> Needs 2 '(' for the middle ')' and 2 ')' for the trailing '('. Result: 4
    sol.minAddToMakeValid("()))((")
    