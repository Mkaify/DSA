class Solution:
    def minPartitions(self, s: str) -> int:
        """
        Partitions the string into the minimum number of substrings such that
        each substring contains unique characters.
        
        Algorithm:
        Greedy approach - try to make each substring as long as possible.
        Traverse the string and maintain a set of characters seen in the current 
        partition. If a character is encountered that is already in the set, 
        start a new partition and reset the set.
        
        Time Complexity: O(n) - Single pass through the string.
        Space Complexity: O(1) - The set will store at most 26 unique characters.
        """
        # We always need at least one partition if the string is not empty.
        # The constraints say 1 <= s.length, so we start at 1.
        partitions = 1
        seen_chars = set()
        
        for char in s:
            # If the character is already in the current substring,
            # we must start a new trick/maze (substring).
            if char in seen_chars:
                partitions += 1
                # Start fresh with the new character as the first in the new set
                seen_chars = {char}
            else:
                # Add the character to the current unique set
                seen_chars.add(char)
                
        return partitions

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: "abacaba"
    # Logic: "ab", "ac", "ab", "a" (or similar unique partitions)
    # Output: 4
    sol.minPartitions('abacaba')
    
    # Example 2: "ssssss"
    # Logic: Every 's' must be its own partition
    # Output: 6
    sol.minPartitions('ssssss')
    
    # Example 3: "abcde"
    # Logic: Entire string is unique
    # Output: 1
    sol.minPartitions('abcde')
