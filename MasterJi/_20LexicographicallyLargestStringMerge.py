class Solution:
    def lexicographicallyLargestMerge(self, word1: str, word2: str) -> str:
        '''
        word1: str - the first word
        word2: str - the second word
        returns: str - the lexicographically largest merge
        '''
        # Your implementation here
        merge = []
        i, j = 0, 0
        n1, n2 = len(word1), len(word2)
        
        while i < n1 and j < n2:
            # Compare the remaining suffixes of both words
            # String comparison word1[i:] > word2[j:] handles the case 
            # where the first characters are identical.
            if word1[i:] > word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        
        # Append the remaining characters of the non-empty word
        if i < n1:
            merge.append(word1[i:])
        if j < n2:
            merge.append(word2[j:])
            
        return "".join(merge)
    
# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    # word1 = "dacaa", word2 = "dbaaa"
    # Result: "ddbacaaaaa"
    sol.lexicographicallyLargestMerge('dacaa', 'dbaaa')
    
    # Example 2
    # word1 = "abcabc", word2 = "abcbca"
    # Result: "abcbcaabcabc"
    sol.lexicographicallyLargestMerge('abcabc', 'abcbca')
    
    # Example 3
    # word1 = "abc", word2 = "ab"
    # Result: "abcab"
    sol.lexicographicallyLargestMerge('abc', 'ab')                    