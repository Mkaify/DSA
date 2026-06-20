class Solution:
    def count_object_types(self, objects):
        '''
        objects: list of strings representing different objects
        '''
        counts = {}

        for item in objects:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
            
        return counts


if __name__ == "__main__":
    
    organizer = Solution()
    
    # Example 1: Toy models
    toys = ["car", "doll", "car", "puzzle", "doll", "car"]
    organizer.count_object_types(toys)
    # Expected: {"car": 3, "doll": 2, "puzzle": 1}
    
    # Example 2: Fruits
    fruits = ["apple", "banana", "apple", "orange", "banana", "banana"]
    organizer.count_object_types(fruits)
    # Expected: {"apple": 2, "banana": 3, "orange": 1}
    
    # Example 3: Large list simulation
    large_list = ["item_a"] * 50000 + ["item_b"] * 50000
    organizer.count_object_types(large_list)
    # print(f"item_a={result['item_a']}, item_b={result['item_b']}"