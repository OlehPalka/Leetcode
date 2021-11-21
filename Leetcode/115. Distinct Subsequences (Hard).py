class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        s = " " + s
        t = " " + t
        t_len = len(t)
        s_len = len(s)
        dp = [[1 if j == 0 else 0 for i in range(s_len)] for j in range(t_len)]

        for col_letter_idx in range(1, t_len):

            for row_letter_idx in range(1, s_len):

                if t[col_letter_idx] == s[row_letter_idx]:
                    dp[col_letter_idx][row_letter_idx] = dp[col_letter_idx -
                                                            1][row_letter_idx - 1] + dp[col_letter_idx][row_letter_idx - 1]
                else:
                    dp[col_letter_idx][row_letter_idx] = dp[col_letter_idx][row_letter_idx - 1]

        return dp[col_letter_idx][row_letter_idx]
