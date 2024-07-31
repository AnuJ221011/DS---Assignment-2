#https://leetcode.com/problems/design-a-stack-with-increment-operation/submissions/1277757593/
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize=maxSize
        self.st=[]
        self.size=0
        self.count=0

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.st.append(x)
            self.size+=1

    def pop(self) -> int:
        if self.size<1:
            return -1
        else:
            self.size -= 1
            return self.st.pop()

    def increment(self, k: int, val: int) -> None:
        st2=[]
        if self.size <= k:
            while self.st:
                st2.append(self.st.pop()+val)
            while st2:
                self.st.append(st2.pop())
        else:
            while self.st:
                st2.append(self.st.pop())   
            
            while st2:
                if self.count<k:
                    self.st.append(st2.pop()+val)
                    self.count += 1
                else:
                    self.st.append(st2.pop())
                    self.count += 1

            self.count=0

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)