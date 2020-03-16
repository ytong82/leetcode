class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for index in range(coin, amount+1):
                dp[index] += dp[index-coin]
        return dp[amount]


amount = 5
coins = [1, 2, 5]

amount = 3
coins = [2]

amount = 10
coins = [10]

sol = Solution()
print(sol.change(amount, coins))