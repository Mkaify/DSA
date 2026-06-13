class Solution:
    def selectLongerStrings(self, words, k):
        '''
        words: array of strings to be evaluated
        k: the integer length threshold
        '''
        # Your implementation here
        return [word for word in words if len(word)>k]

if __name__ == "__main__":
    sol = Solution()
    words1 = ['dog', 'elephant', 'cat', 'grocerystore']
    k1 = 3

    sol.selectLongerStrings(words1, k1)

    words2 = ['a', 'an', 'the', 'quick']
    k2 = 2
    sol.selectLongerStrings(words2, k2)

    words3 = ['flowers', 'sun', 'moon', 'river']
    k3 = 4
    sol.selectLongerStrings(words3, k3)