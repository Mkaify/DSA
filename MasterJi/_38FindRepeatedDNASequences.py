from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        Finds all 10-letter-long sequences (substrings) that occur more than once.
        
        VocloneTranslate Analogy:
        Detecting these repeating subsegments behaves exactly like tracking 
        duplicated audio frames or phoneme vectors to optimize translation 
        models or sequence alignments.
        
        Time Complexity: O(N) where N is the length of s (since sliding window length is a constant L = 10).
        Space Complexity: O(N) to store the unique sequences in hash sets.
        """
        seen = set()
        repeated = set()
        
        # Slide a window of size 10 across the sequence
        for i in range(len(s) - 9):
            sub_seq = s[i:i+10]
            
            # If we've already encountered this sequence, it's a repeat
            if sub_seq in seen:
                repeated.add(sub_seq)
            else:
                # Otherwise, record that we have seen it
                seen.add(sub_seq)
                
        return list(repeated)

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: DNA sequence with multiple overlapping repeats
    s1 = "TTTTTGGGGGTTTTTGGGGGTTTTTAAACCC"
    sol.findRepeatedDnaSequences(s1)
    
    # Example 2: Continuous sequence of identical nucleotides
    s2 = "GGGGGGGGGGGG"
    sol.findRepeatedDnaSequences(s2)