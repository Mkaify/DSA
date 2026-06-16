class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        This algorithm uses the Dutch National Flag approach with three pointers:
        - low: Boundary for the 0s (red)
        - mid: Current element being evaluated
        - high: Boundary for the 2s (blue)
        
        Time Complexity: O(n) - Single pass
        Space Complexity: O(1) - Constant extra space
        """
        if not nums:
            return

        low = 0
        mid = 0
        high = len(nums) - 1
        
        # We iterate until the mid pointer passes the high pointer.
        # Everything after high is guaranteed to be 2.
        # Everything before low is guaranteed to be 0.
        while mid <= high:
            if nums[mid] == 0:
                # If we find a 0, move it to the 'low' section
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1s stay in the middle, just move to the next element
                mid += 1
            else: # nums[mid] == 2
                # If we find a 2, move it to the 'high' section.
                # Crucially, we don't increment mid here because the new 
                # element swapped from the back needs to be evaluated.
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums1)    
    
    # Example 2
    nums2 = [2, 0, 1]
    sol.sortColors(nums2)    
    
    # Example 3 (All same)
    nums3 = [1, 1, 1]
    sol.sortColors(nums3)
    
    # Example 4 (Already sorted)
    nums4 = [0, 1, 2]
    sol.sortColors(nums4)