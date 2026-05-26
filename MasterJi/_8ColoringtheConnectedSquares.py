from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Performs a flood fill on the image starting from (sr, sc).
        
        Time Complexity: O(m * n) - where m is rows and n is columns.
        Space Complexity: O(m * n) - for the recursion stack.
        """
        rows = len(image)
        cols = len(image[0])
        start_color = image[sr][sc]
        
        # If the starting pixel already has the target color, 
        # no changes are needed. This also prevents infinite recursion.
        if start_color == color:
            return image
        
        def fill(r, c):
            # Check boundary conditions and color match
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                image[r][c] != start_color):
                return
            
            # Update the current pixel color
            image[r][c] = color
            
            # Recurse for the four adjacent neighbors (up, down, left, right)
            fill(r + 1, c) # Down
            fill(r - 1, c) # Up
            fill(r, c + 1) # Right
            fill(r, c - 1) # Left
            
        # Start the fill process from the specified starting pixel
        fill(sr, sc)
        return image

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr1, sc1, color1 = 1, 1, 2
    # Result: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    sol.floodFill(image1, sr1, sc1, color1)
    
    # Example 2
    image2 = [[0, 0, 0], [0, 0, 0]]
    sr2, sc2, color2 = 0, 0, 0
    # Result: [[0, 0, 0], [0, 0, 0]]
    sol.floodFill(image2, sr2, sc2, color2)