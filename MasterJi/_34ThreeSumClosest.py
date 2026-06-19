class Solution:
    def closestThreeSum(self, nums: list[int], target: int) -> int:
        """
        Finds the sum of three integers in nums closest to the target.
        
        Time Complexity: O(n^2) - Sorting takes O(n log n), nested loops take O(n^2).
        Space Complexity: O(1) or O(n) depending on the sorting implementation.
        """
        # Step 1: Sort the array to enable the two-pointer approach
        nums.sort()
        n = len(nums)
        
        # Initialize with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            # Optimization: Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Use two pointers for the remaining two elements
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we found the exact target, return immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if the current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on how the sum compares to the target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: [-1, 2, 1, -4], target = 1
    # Sorted: [-4, -1, 1, 2]. Closest sum: -1 + 1 + 2 = 2
    sol.closestThreeSum([-1, 2, 1, -4], 1)
    
    # Example 2: [0, 0, 0], target = 1
    # Only one possibility: 0 + 0 + 0 = 0
    sol.closestThreeSum([0, 0, 0], 1)
    
    # Example 3: [1, 1, 1, 0], target = -100
    # Smallest sum is 0 + 1 + 1 = 2
    sol.closestThreeSum([1, 1, 1, 0], -100)