def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)):
            if i == 0 or prices[i] < prices[i - 1]:
                for j in range(len(prices) - 1, i, -1):
                    if prices[j] - prices[i] > profit:
                        profit = prices[j] - prices[i]
        return profit

print(maxProfit([1,2])) 