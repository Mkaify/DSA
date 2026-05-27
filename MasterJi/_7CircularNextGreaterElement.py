class Solution:
    def nextGreaterElements(self, nums):
        '''
        nums: List[int] - An array of integers representing the circular array
        Returns a List[int] representing the next greater element for each index
        '''
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2*n):
            curr_idx = i % n
            curr_num = nums[curr_idx]

            while stack and nums[stack[-1]] < curr_num:
                last_idx = stack.pop()
                res[last_idx] = curr_num

            if i < n:
                stack.append(curr_idx)        
                
        return res

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: [2, 5, 3]
    # Expected: [5, -1, 5]
    sol.nextGreaterElements([2, 5, 3])
    
    # Example 2: [4, 1, 2, 3]
    # Expected: [-1, 2, 3, 4]
    sol.nextGreaterElements([4, 1, 2, 3])
    
    # Example 3: All same numbers [1, 1, 1]
    # Expected: [-1, -1, -1]
    sol.nextGreaterElements([1, 1, 1])

    # Example 4: Strictly decreasing [5, 4, 3, 2, 1]
    # The '5' will be the next greater for all after wrapping around
    sol.nextGreaterElements([5, 4, 3, 2, 1])
