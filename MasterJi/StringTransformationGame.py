class Solution:
    def stringTransformationGame(self, t, cases):
        '''
        t: number of test cases
        cases: list of strings for each test case
        Returns: a list of transformed strings
        '''
        results = []
        
        for s in cases:
            # Convert string to list because strings are immutable in Python
            chars = list(s)
            n = len(chars)
            
            for i in range(n):
                # Even Index (0, 2, 4...) -> Hitesh's Turn
                # Goal: Make lexicographically smallest ('a')
                if i % 2 == 0:
                    if chars[i] == 'a':
                        chars[i] = 'b' # Forced to change 'a' -> 'b'
                    else:
                        chars[i] = 'a' # Change anything else -> 'a'
                
                # Odd Index (1, 3, 5...) -> Piyush's Turn
                # Goal: Make lexicographically largest ('z')
                else:
                    if chars[i] == 'z':
                        chars[i] = 'y' # Forced to change 'z' -> 'y'
                    else:
                        chars[i] = 'z' # Change anything else -> 'z'
            
            # Join list back to string and add to results
            results.append("".join(chars))
            
        return results

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Input Example
    t = 3
    cases = ["a", "bbbb", "az"]
    
    # Get results
    sol.stringTransformationGame(t, cases)
    
    # # Print results
    # for res in output:
    #     print(res)
    
    # # Expected Output:
    # b
    # azaz
    # by