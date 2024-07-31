#https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/submissions/1277588205/
class RandomizedCollection:

    def __init__(self):
        self.lst=[]
        self.size=0

    def insert(self, val: int) -> bool:
        self.size+=1
        if val not in self.lst:
            self.lst.append(val)
            return True

        self.lst.append(val)
        return False

    def remove(self, val: int) -> bool:
        if val in self.lst:
            self.lst.remove(val)
            self.size-=1
            return True

        return False

    def getRandom(self) -> int:
        return self.lst[randint(0,self.size-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()