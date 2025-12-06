class Solution:
    def findErrorNums(self, nums):
        '''
        nums: List[int] - an array of integers where one number is duplicated and one is missing
        '''
        n = len(nums)

        count = [0] * (n+1)

        for num in nums:
            count[num] +=1
            

        duplicate = -1
        missing = -1

        for i in range(1,n+1):
            if count[i] ==2:
                duplicate =i
            elif count[i]==0:
                missing = i

        return [duplicate, missing]

if __name__ == "__main__":
    sol = Solution()
    sol.findErrorNums([1,2,2,4])
    sol.findErrorNums([1,2,2])
        # return [0, 0]  # Replace with the correct numbers
