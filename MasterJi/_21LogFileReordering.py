class Solution:
    def reorderLogFiles(self, logs):
        '''
        logs: List[str] - List of log strings
        return: List[str] - Reordered list of log strings
        '''
        letter_logs = []
        digit_logs = []

        for log in logs:                        
            parts = log.split(" ", 1)

            if parts[1][0].isdigit():
                digit_logs.append(log)

            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ",1)[0]))
        return letter_logs + digit_logs

if __name__ == "__main__":
    sol = Solution()
    logs1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    logs2 = ["a1 9 2 3 1", "g1 act car"]
    logs3 = ["a1 art can", "b1 art can", "dig1 1 2 3"]

    sol.reorderLogFiles(logs1)
    sol.reorderLogFiles(logs2)
    sol.reorderLogFiles(logs3)
    
    