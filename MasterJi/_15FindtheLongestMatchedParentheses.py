class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        s: str - the parentheses string
        Return the length of the longest valid parentheses substring
        '''
        stack = [-1]
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)

                else:
                    current_length = i - stack[-1]
                    if current_length > max_length:
                        max_length = current_length
        return max_length

if __name__ == "__main__":
    sol = Solution()

    sol.longestValidParentheses("(()")
    sol.longestValidParentheses(")()())")
    sol.longestValidParentheses("")
    sol.longestValidParentheses("()(()")
    sol.longestValidParentheses("()(())")
