class Solution:
    def baseballScoreTracker(self, operations: list[str]) -> int:
        '''
        operations: List[str] - a list of operations to apply to the score record
        Returns the total score after applying all operations
        '''
        record = []
        
        for op in operations:
            if op == '+':
                # Sum the last two scores
                if len(record) >= 2:
                    new_score = record[-1] + record[-2]
                    record.append(new_score)
                
            elif op == 'D':
                # Double the last score
                if len(record) >= 1:
                    new_score = record[-1] * 2
                    record.append(new_score)
                
            elif op == 'C':
                # Cancel/Remove the last score
                if len(record) >= 1:
                    record.pop()
                
            else:
                # Try to convert to integer (handles "5", "-2", etc.)
                # If op is "-", int() raises ValueError, so we catch it and skip.
                try:
                    record.append(int(op))
                except ValueError:
                    continue
                
        return sum(record)

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    ops1 = ["5","2","C","D","+"]
    sol.baseballScoreTracker(ops1)
    # Expected: 30

    # Example 2 (Includes negative numbers)
    ops2 = ["5","-2","4","C","D","9","+","+"]
    sol.baseballScoreTracker(ops2)
    # Expected: 27
    
    # Test case that previously crashed (Standalone "-")
    ops_crash = ["5", "-", "2"] 
    # Logic: Adds 5. Skips "-". Adds 2. Sum = 7.
    sol.baseballScoreTracker(ops_crash)