from typing import List

class Solution:
    def candyCountDifference(self, nums: List[int]) -> List[int]:
        """
        Calculates the summation of absolute differences between each element 
        and all other elements in a sorted array using Prefix and Suffix sums.
        
        VocloneTranslate Analogy:
        Optimizes alignment distance calculation between pitch frames by avoiding 
        O(N^2) comparisons, crucial for low-latency neural acoustic models.
        
        Time Complexity: O(N) - A single pass to compute total sum, and a single pass to build result.
        Space Complexity: O(1) - Beyond the output array, we only use a few tracking variables.
        """
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        result = []
        
        for i, num in enumerate(nums):
            # Calculate suffix sum on the fly
            right_sum = total_sum - left_sum - num
            
            # Count of elements to the left and right
            left_count = i
            right_count = n - 1 - i
            
            # Apply our prefix and suffix formulas
            left_diff = (num * left_count) - left_sum
            right_diff = right_sum - (num * right_count)
            
            # Combine the differences
            result.append(left_diff + right_diff)
            
            # Accumulate current element to the prefix sum
            left_sum += num
            
        return result

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    # Inputs: nums = [2, 3, 5]
    sol.candyCountDifference([2, 3, 5])
    
    # Example 2
    # Inputs: nums = [1, 4, 6, 8, 10]
    sol.candyCountDifference([1, 4, 6, 8, 10])