class Solution:
    def longestPalindrome(self, str):
        length = len(str)
        if length <= 1:
            return str

        self.str = str
        self.length = length

        mlp = 0
        start = 0
        for i in range(length):
            lp = max(self.getLongestPalindrome(i, i), self.getLongestPalindrome(i, i+1))
            if lp > mlp:
                mlp = lp
                start = i - (lp - 1) // 2

        return str[start:start+mlp]

    def getLongestPalindrome(self, i, j):
        while i >= 0 and j < self.length and self.str[i] == self.str[j]:
            i -= 1
            j += 1
        return j - i - 1


str = "cbabadabab"
sol = Solution()
print(sol.longestPalindrome(str))








