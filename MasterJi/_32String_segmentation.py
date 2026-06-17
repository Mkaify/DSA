class Solution:
    def stringSegmentation(self, s: str, wordDict: list) -> bool:
        '''
        s: the input string to be segmented
        wordDict: list of strings representing the dictionary
        Returns: boolean indicating if s can be segmented using words in wordDict
        '''
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]


if __name__ == "__main__":
    sol = Solution()

    str(sol.stringSegmentation('traintrack', ['train', 'track'])).lower()
    str(sol.stringSegmentation('ballflowerball', ['ball', 'flower'])).lower()
    str(sol.stringSegmentation('catsandprince', ['cats', 'prince', 'sand', 'and', 'cat'])).lower()
    str(sol.stringSegmentation('catsanddog', ['cats', 'dog'])).lower()
