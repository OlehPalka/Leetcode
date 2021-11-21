class Solution:
    def minCut(self, s: str) -> int:

        is_palindrom = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            is_palindrom[i][i] = True

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                is_palindrom[i][i+1] = True

        for i in range(2, len(s)):
            begining = 0
            end = i

            while end < len(s):
                if s[begining] == s[end] and is_palindrom[begining + 1][end - 1]:
                    is_palindrom[begining][end] = True

                begining += 1
                end += 1

        dp = [len(s)] * (len(s) + 1)
        dp[-1] = 0

        for win_begin in range(len(s) - 1, -1, -1):

            for win_end in range(win_begin, len(s)):

                if is_palindrom[win_begin][win_end]:
                    dp[win_begin] = min(dp[win_begin], dp[win_end + 1] + 1)

        return dp[0] - 1
