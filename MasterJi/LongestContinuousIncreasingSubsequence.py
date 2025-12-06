class Solution:
    def findLongestGrowingStretch(self, nums):
        '''
        nums: List[int] -- an unsorted array of integers
        Returns the length of the longest continuous increasing subsequence
        '''
        if not nums:
            return 0

        maxLen = 1
        currentLen =1

        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                currentLen +=1
            else:
                currentLen =1

            maxLen = max(maxLen, currentLen)
        return maxLen

if __name__ == "__main__":
    sol = Solution()
    sol.findLongestGrowingStretch([1,3,5,4,7])
    sol.findLongestGrowingStretch([2,2,2,2,2])
    sol.findLongestGrowingStretch([10])
