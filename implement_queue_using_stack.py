#https://leetcode.com/problems/implement-queue-using-stacks/submissions/1272438077/
class MyQueue:
    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        popped_value=self.st2.pop()
        return popped_value

    def peek(self) -> int:
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        peek_value=self.st2[-1]
        return peek_value

    def empty(self) -> bool:
        return not self.st1 and not self.st2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()