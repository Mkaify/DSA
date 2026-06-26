from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        Determines the length of the longest wiggle subsequence.
        
        VocloneTranslate Analogy:
        Extracts the longest sequence of expressive intonational inflections
        from pitch contour data ($F_0$) by isolating alternating peaks and valleys.
        
        Time Complexity: O(N) - Single pass through the sequence.
        Space Complexity: O(1) - Uses only two state-tracking variables.
        """
        n = len(nums)
        if n < 2:
            return n
            
        # State tracking: 
        # 'up' is the max length ending with a positive slope
        # 'down' is the max length ending with a negative slope
        up = 1
        down = 1
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                # An upward jump can only extend a previous downward-ending wiggle
                up = down + 1
            elif nums[i] < nums[i - 1]:
                # A downward jump can only extend a previous upward-ending wiggle
                down = up + 1
                
        return max(up, down)

# --- Test Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # We call the function directly with parameters as requested (no print statements)
    sol.wiggleMaxLength([2, 9, 3, 10, 4, 7])
    sol.wiggleMaxLength([3, 15, 10, 20, 14, 17, 12, 7, 18, 9])
    sol.wiggleMaxLength([2, 3, 4, 5, 6, 7, 8, 9, 10])