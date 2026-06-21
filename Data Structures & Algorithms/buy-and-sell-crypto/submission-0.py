class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit_l = []
        while i<len(prices):
            pot_buy = prices[i]
            pot_profit_l = []
            j = i+1
            while j<len(prices):
                pot_sell = prices[j]
                if pot_sell<pot_buy:
                    j+=1
                else:
                    pot_profit_l.append(pot_sell-pot_buy)
                    j+=1
            if len(pot_profit_l)>0:
                profit_l.append(max(pot_profit_l))
            i+=1
        return max(profit_l) if len(profit_l)>0 else 0
        