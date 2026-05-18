class Solution:
    def superEggDrop(self, k, n):
        '''
        k: number of eggs
        n: number of floors
        '''
        dp = [0] * (k+1)
        m = 0

        while dp[k] < n:
            m+=1

            for j in range(k, 0, -1):
                dp[j] = dp[j-1] + dp[j] + 1
        return m

if __name__ == "__main__":
    sol = Solution()
    sol.superEggDrop(1,2)
    sol.superEggDrop(2,6)
    sol.superEggDrop(3,12)
    sol.superEggDrop(100,1000)
                
