class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """
        Simulates asteroid collisions using a stack.
        
        Time Complexity: O(n) - Each asteroid is pushed and popped at most once.
        Space Complexity: O(n) - To store the remaining asteroids in the stack.
        """
        stack = []
        
        for ast in asteroids:
            # A collision can only happen if:
            # 1. The stack is not empty
            # 2. The current asteroid is moving LEFT (negative)
            # 3. The asteroid at the top of the stack is moving RIGHT (positive)
            while stack and ast < 0 < stack[-1]:
                # Collision logic:
                # Compare absolute sizes
                if stack[-1] < -ast:
                    # The right-moving asteroid in the stack is smaller, it explodes
                    stack.pop()
                    # Continue checking the next element in the stack against the current 'ast'
                    continue
                elif stack[-1] == -ast:
                    # Both are the same size, both explode
                    stack.pop()
                
                # If stack[-1] >= -ast, the current asteroid 'ast' explodes.
                # We break because the current 'ast' is gone.
                break
            else:
                # This 'else' belongs to the 'while' loop. 
                # It executes if the while loop finishes without a 'break'.
                # That happens if:
                # - No collision was possible (e.g., both moving same way or stack empty)
                # - The current asteroid destroyed all right-moving obstacles in its path
                stack.append(ast)
                
        return stack

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: [6, 13, -4]
    # 13 and -4 collide -> 13 survives.
    sol.asteroidCollision([6, 13, -4])
    # Expected: [6, 13]
    
    # Example 2: [7, -7]
    # Both explode.
    sol.asteroidCollision([7, -7])
    # Expected: []
    
    # Example 3: [11, 3, -6]
    # -6 destroys 3, then -6 is destroyed by 11.
    sol.asteroidCollision([11, 3, -6])
    # Expected: [11]
    
    # Example 4: Multiple collisions
    # [-2, -1, 1, 2] -> No collisions (moving away from each other)
    sol.asteroidCollision([-2, -1, 1, 2]) 
    # Expected: [-2, -1, 1, 2]