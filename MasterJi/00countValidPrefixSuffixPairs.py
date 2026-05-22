class Solution:
    def countValidPrefixSuffixPairs(self, words: list[str]) -> int:
        """
        Counts pairs (i, j) such that i < j and words[i] is both a prefix 
        and suffix of words[j].
        
        Time Complexity: O(Sum of lengths of all words)
        Space Complexity: O(Sum of lengths of all words)
        """
        
        # Helper function to compute Z-array
        # z[i] is the length of the longest common prefix between s and the suffix of s starting at i.
        def get_z_array(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            z[0] = n
            return z

        # Trie structure: A dictionary of dictionaries.
        # Each node has a specialized key '_count' to store how many words end there.
        root = {'_count': 0}
        total_pairs = 0
        
        for word in words:
            n = len(word)
            
            # 1. Compute Z-array for the current word to help with suffix checks
            z = get_z_array(word)
            
            # 2. Traverse the Trie to find existing words that are prefixes of current word
            node = root
            for i, char in enumerate(word):
                if char not in node:
                    break
                node = node[char]
                
                # If a previous word ends here, it is a prefix of 'word'
                count = node.get('_count', 0)
                if count > 0:
                    # Check if this prefix is also a suffix using the Z-array
                    # The prefix has length i+1.
                    # The suffix of 'word' starting at index (n - (i+1)) must match the prefix.
                    length_of_prefix = i + 1
                    suffix_start_index = n - length_of_prefix
                    
                    if z[suffix_start_index] == length_of_prefix:
                        total_pairs += count
            
            # 3. Insert the current word into the Trie
            node = root
            for char in word:
                if char not in node:
                    node[char] = {'_count': 0}
                node = node[char]
            node['_count'] += 1
            
        return total_pairs

# --- Test Cases ---
if __name__ == "__main__":
    sol= Solution()
    sol.countValidPrefixSuffixPairs(['x', 'xyx', 'xyzxy', 'yy'])
    sol.countValidPrefixSuffixPairs(['na', 'nana', 'ya', 'yaya'])
    sol.countValidPrefixSuffixPairs(['pqrpqr', 'pqr'])
    sol.countValidPrefixSuffixPairs(['a', 'a', 'a'])