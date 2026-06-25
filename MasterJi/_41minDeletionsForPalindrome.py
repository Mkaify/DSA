class Solution:
    def minDeletionsForPalindrome(self, s: str) -> int:
        """
        Calculates the minimum number of character deletions required to 
        transform string s into a palindrome.
        
        VocloneTranslate Analogy:
        Isolates the core symmetric acoustic reflection patterns in a 
        reverberant speech signal by identifying and stripping out asymmetric noise.
        
        Time Complexity: O(N^2) - Where N is the length of the string.
        Space Complexity: O(N^2) - To store the 2D state transition table.
        """
        n = len(s)
        if n < 2:
            return 0
            
        # dp[i][j] will store the length of the Longest Palindromic Subsequence in s[i..j]
        dp = [[0] * n for _ in range(n)]
        
        # Base Case: Substrings of length 1 are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1
            
        # Build the table bottom-up for substrings of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    # Characters match; extend the internal palindrome by 2
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Characters mismatch; take the maximum by dropping either end
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    
        # Length of the Longest Palindromic Subsequence of s
        lps_length = dp[0][n - 1]
        
        # Minimum deletions is the difference between total length and LPS length
        return n - lps_length

# --- Test Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Executing directly with parameters as requested (no print statements)
    sol.minDeletionsForPalindrome("xayzbayx")
    sol.minDeletionsForPalindrome("madam")
    sol.minDeletionsForPalindrome("aabbcc")