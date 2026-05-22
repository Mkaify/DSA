class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """
        Finds the maximum number of fruits that can be collected in two baskets.
        This is equivalent to finding the longest subarray with at most 2 distinct elements.
        
        Time Complexity: O(n) - Each element is visited at most twice (by left and right pointers).
        Space Complexity: O(1) - The hash map stores at most 3 distinct fruit types at any time.
        """
        # Hash map to store the frequency of each fruit type in the current window
        basket = {}
        left = 0
        max_fruits = 0
        
        # 'right' pointer expands the window
        for right in range(len(fruits)):
            fruit_type = fruits[right]
            basket[fruit_type] = basket.get(fruit_type, 0) + 1
            
            # If we have more than 2 types of fruits, shrink the window from the left
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                
                # If a fruit type's count drops to 0, remove it from the basket
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                
                # Move the left boundary forward
                left += 1
            
            # The current window [left...right] contains at most 2 types of fruits
            # Calculate the length of the window and update max_fruits
            current_window_size = right - left + 1
            if current_window_size > max_fruits:
                max_fruits = current_window_size
                
        return max_fruits

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: [1, 2, 1]
    # Window can be the entire array. Output: 3
    sol.totalFruit([1, 2, 1])
    
    # Example 2: [0, 1, 2, 2]
    # Window [1, 2, 2] has two types (1 and 2). Output: 3
    sol.totalFruit([0, 1, 2, 2])
    
    # Example 3: [1, 2, 3, 2, 2]
    # Window [2, 3, 2, 2] has two types (2 and 3). Output: 4
    sol.totalFruit([1, 2, 3, 2, 2])
    
    # Example 4: [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    # Longest sub-segment is [1, 2, 1, 1, 2] -> 5
    sol.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])