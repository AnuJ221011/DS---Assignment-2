#https://leetcode.com/problems/online-stock-span/submissions/1277733462/
class StockSpanner:

    def __init__(self):
        self.stack = [] 

    def next(self, price: int) -> int:
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_count = self.stack.pop()
            count += prev_count
        self.stack.append((price, count))
        return count

        
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)