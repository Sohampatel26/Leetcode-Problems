class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1

        for c in coins:
            for i in range(1,amount+1):
                if i-c>=0:
                    dp[i]=dp[i-c]+dp[i]
        return dp[-1]

        