from typing import List

class Solution:
    def maximizeJobProfit(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """
        Calculates the maximum possible profit by optimally assigning workers to jobs.
        
        VocloneTranslate Analogy:
        Assigns real-time speech synthesis channels (workers with varying compute capacities) 
        to acoustic frame processing tasks (jobs with difficulty and output fidelity gain)
        to maximize overall vocal output quality.
        
        Time Complexity: O(N log N + M log M) - where N is the number of jobs and M is the number of workers.
        Space Complexity: O(N) - to store the paired job profiles.
        """
        # Step 1: Pair difficulty and profit together, then sort them by difficulty
        jobs = sorted(zip(difficulty, profit))
        
        # Step 2: Sort workers by their processing capability
        worker.sort()
        
        total_profit = 0
        max_profit_so_far = 0
        job_idx = 0
        n_jobs = len(jobs)
        
        # Step 3: Iterate through each worker
        for ability in worker:
            # While there are available jobs that the current worker can perform
            while job_idx < n_jobs and jobs[job_idx][0] <= ability:
                # Track the best profit we can make up to this difficulty level
                max_profit_so_far = max(max_profit_so_far, jobs[job_idx][1])
                job_idx += 1
            
            # Add the best achievable profit for this worker to the total accumulation
            total_profit += max_profit_so_far
            
        return total_profit

# --- Test Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Executing directly with parameters as requested (no print statements)
    sol.maximizeJobProfit([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])
    sol.maximizeJobProfit([85, 47, 57], [24, 66, 99], [40, 25, 25])