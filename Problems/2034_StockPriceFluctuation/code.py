from heapq import heappop, heappush
from typing import List
from sortedcontainers import SortedDict, SortedList


class StockPrice2:

    def __init__(self):
        self.pricesSorted: SortedDict[int] = SortedDict() # just for prices; {4058, 1}
        self.recordsDict: dict[int, int] = {} # dictionary for all records, ts is key
        self.latestRecordTimestamp = 0

        # Use SortedDict from SortedContainers
        # Ops are in O(logn); uses balanced binary tree under the hood
        

    def update(self, timestamp: int, price: int) -> None:
        # this automatically updates values as they're sent in
        #self.records[timestamp] = price

        # update the current
        # we're never removing a timestamp, so do a simple comparison
        if timestamp > self.latestRecordTimestamp:
            self.latestRecordTimestamp = timestamp

        # if this timestamp already has a record associated with it
        if timestamp in self.recordsDict:
            old = self.recordsDict[timestamp] # find the old price
            self.pricesSorted[old] -= 1 # this is falsey

            if not self.pricesSorted[old]: # if the value is falsey (the -1 from above)
                del self.pricesSorted[old]

        self.recordsDict[timestamp] = price

        if price in self.pricesSorted:
            self.pricesSorted[price] += 1
        else:
            self.pricesSorted[price] = 1



    def current(self) -> int:
        print(list(self.records.keys()))
        print(self.records)
        return self.recordsDict[self.latestRecordTimestamp]
        # return self.records[self.latestRecordTimestamp]

        # this sort is too slow
        # return self.records[sorted(list(self.records.keys()))[-1]]
        # return self.stockRecords[-1][1]


    def maximum(self) -> int:
        # max: int = 0
        # for key in self.records.keys():
        #     if self.records[key] > max:
        #         max = self.records[key]
            
        # return self.records[self.maxValueTimestamp]
        print(self.pricesSorted.keys())
        return list(self.pricesSorted.keys())[-1]
        # max: int = 0
        # for record in self.stockRecords:
        #     if record[1] > max:
        #         max = record[1]
        
        # return max


    def minimum(self) -> int:
        # min: int = self.maximum()
        # for key in self.records.keys():
        #     if self.records[key] < min:
        #         min = self.records[key]
            
        # return self.records[self.minValueTimestamp]
        return list(self.pricesSorted.keys())[0]
        # min: int = 0
        # for record in self.stockRecords:
        #     if record[1] < min:
        #         min = record[1]

        # return min
    

    def showAllRecords(self) -> List[List[int]]:
        return self.records


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


# obj = StockPrice()
# obj.update(1, 10)
# print(obj.showAllRecords())
# obj.update(2, 5)
# print(obj.showAllRecords())
# c1 = obj.current()
# print(c1)
# m1 = obj.maximum()
# print(m1)
# obj.update(1, 3)
# print(obj.showAllRecords())
# param_3 = obj.maximum()
# print(param_3)
# obj.update(4, 2)
# print(obj.showAllRecords())
# param_4 = obj.minimum()
# print(param_4)

# s = StockPrice()
# s.update(1, 10)
# print(s.showAllRecords())
# s.update(2, 5)
# print(s.showAllRecords())
# print(s.current())
# print(s.maximum())
# s.update(1,3)
# print(s.showAllRecords())
# print(s.maximum())
# s.update(4, 2)
# print(s.showAllRecords())
# print(s.minimum())
# s.update(38,2308)
# s.update(47,7876)
# s.update(58,1866)
# s.update(43,6141)
# s.update(36,3192)
# print(s.current())
# print(s.maximum())
# print(s.minimum())







class StockPrice:
    def __init__(self):
        self.latest_time = 0
        # Store price of each stock at each timestamp.
        self.timestamp_price_map = {}
        
        # Store stock prices in sorted order to get min and max price.
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        # Update latestTime to latest timestamp.
        self.timestamp_price_map[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)

        # Add latest price for timestamp.
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        # Return latest price of the stock.
        return self.timestamp_price_map[self.latest_time]

    def maximum(self) -> int:
        price, timestamp = self.max_heap[0]

        # Pop pairs from heap with the price doesn't match with hashmap.
        # Max Heap: (-10, 1), (-3, 1) -> (-3, 1)
        # Dict: {1: 3}
        while -price != self.timestamp_price_map[timestamp]:
            heappop(self.max_heap)
            price, timestamp = self.max_heap[0]
            
        return -price

    def minimum(self) -> int:
        price, timestamp = self.min_heap[0]

        # Pop pairs from heap with the price doesn't match with hashmap.
        while price != self.timestamp_price_map[timestamp]:
            heappop(self.min_heap)
            price, timestamp = self.min_heap[0]
            
        return price


s = StockPrice()
s.update(1, 10)
# print(s.showAllRecords())
s.update(2, 5)
# print(s.showAllRecords())
print(s.current())
print(s.maximum())
s.update(1,3)
# print(s.showAllRecords())
print(s.maximum())
s.update(4, 2)
# print(s.showAllRecords())
print(s.minimum())
s.update(38,2308)
s.update(47,7876)
s.update(58,1866)
s.update(43,6141)
s.update(36,3192)
print(s.current())
print(s.maximum())
print(s.minimum())