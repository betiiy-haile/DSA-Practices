class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        stack = []
        result = ""

        for i in range(1, n + 2):
            stack.append(str(i)) 
            if i == n + 1 or pattern[i - 1] == 'I':
                while stack:
                    result += stack.pop()  

        return result