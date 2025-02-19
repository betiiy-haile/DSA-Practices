class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_string = []

        def backtrack(curr):
            if len(curr) == n:
                happy_string.append(curr)
                return

            for ch in "abc":
                if curr == "" or curr[-1] != ch:
                    backtrack(curr + ch)

        backtrack("")
        happy_string.sort()
        
        if len(happy_string) >= k:
            return happy_string[k - 1]
        else:
            return ""