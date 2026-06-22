class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        s: str - The original string
        t: str - The string to check as an anagram
        '''
        if len(s) != len(t):            
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            # If count drops below zero, t has more of this character than s
            if count[char] < 0:
                return False

        return True

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    sol.isAnagram("shorthand", "handsorth") # Expected: True
    
    # Example 2
    sol.isAnagram("listen", "silent")      # Expected: True
    
    # Example 3
    sol.isAnagram("apple", "pale")        # Expected: False
    
    # Example 4: Unicode Support
    sol.isAnagram("anagram", "nagaram")    # Expected: True