class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]  # lowest price so far
        profit = 0  # best profit so far

        for p in prices[1:]:  # check prices after day 1
            if buy_price > p:  # found cheaper price
                buy_price = p  # update buy price

            profit = max(profit, p - buy_price)  # sell at p, keep max profit

        return profit  # return best profit
