#https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1277595067/
import random
class RandomizedSet:

    def __init__(self):
        self.lst=[]
        self.size=0
    def insert(self, val: int) -> bool:
        if val not in self.lst:
            self.lst.append(val)
            self.size+=1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.lst:
            self.lst.remove(val)
            self.size-=1
            return True

        return False

    def getRandom(self) -> int:
        return self.lst[randint(0,self.size-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()