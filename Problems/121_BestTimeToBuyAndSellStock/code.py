from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [0] * len(prices)
        maxProfit = 0
        seenPrices = set()
        priceDict = {}
        currentBuyDayMin = 0

        for sellDay in range(1, len(prices)):
            for buyDay in range(0, sellDay):
                print(f"(b: {buyDay}, s: {sellDay}) Bought at ${prices[buyDay]} and now selling at ${prices[sellDay]}")
                # if prices[sellDay] not in priceDict.keys():
                #     priceDict[sellDay] = prices[buyDay]
                #     maxProfit = max(maxProfit, prices[sellDay] - prices[buyDay])
                # elif prices[sellDay] > prices[buyDay]:
                #     maxProfit = max(maxProfit, prices[sellDay] - prices[buyDay])
                #     priceDict[prices[sellDay]] = min(priceDict[prices[sellDay]], prices[buyDay])
                
                # if prices[sellDay] not in priceDict.keys():
                #     priceDict[sellDay] = prices[buyDay]
                #     maxProfit = max(maxProfit, prices[sellDay] - prices[buyDay])
                # elif prices[sellDay] - prices[buyDay] > 0:
                #     maxProfit = max(maxProfit, prices[sellDay] - prices[buyDay])
                #     priceDict[prices[sellDay]] = min(priceDict[prices[sellDay]], prices[buyDay])
                
                # if priceDict[sellDay] not in priceDict.keys() or buyDay >= priceDict[sellDay]:
                
                if (prices[sellDay], prices[buyDay]) not in seenPrices:
                    maxProfit = max(maxProfit, prices[sellDay] - prices[buyDay])
                    seenPrices.add((prices[sellDay], prices[buyDay]))
                    if len(seenPrices) > 100:
                        seenPrices.pop()
        
        return maxProfit
    
s = Solution()
print(s.maxProfit([7,1,5,3,6,4])) # -> 5
print(s.maxProfit([7,6,5,3,1])) # -> 0