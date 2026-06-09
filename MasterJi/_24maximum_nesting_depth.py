class Solution:
    def maxDepth(self, s: str) -> int:        
        max_depth = 0
        current_depth = 0
        
        for char in s:
            if char == '(':
                # Increment depth and update the maximum seen so far
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                # Decrement depth as a pair is closed
                current_depth -= 1
                
        return max_depth

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: "(1+(2*3)+((8)/4))+1" -> Max depth is 3
    print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))    
    # Example 2: "(1)+((2))+(((3)))" -> Max depth is 3
    print(sol.maxDepth("(1)+((2))+(((3)))"))    
    # Example 3: "()(())((()()))" -> Max depth is 3
    print(sol.maxDepth("()(())((()()))"))    
    # Example 4: "1+2+3" -> Max depth is 0
    print(sol.maxDepth("1+2+3"))