'''
You are given an array prices where prices[i] is the price of a given stock 
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
'''


class Solution:
    def maxProfit(self,prices):
        '''
           Complexity O(n)
        '''
        #Two pointers: buy and sell
        left = 0 
        right = 1 
        max_profit = 0
        while right < len(prices):
            #current profit
            currentProfit = prices[right] - prices[left]
            #desirable situation
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else: #otherwise, update left pointer
                left = right
            #update right pointer in one unit
            right += 1
        return max_profit
