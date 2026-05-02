class MyStack:

    def __init__(self):
        self.insertQueue = []
        self.popQueue = []

    def push(self, x: int) -> None:
        self.insertQueue.append(x)
        self.popQueue = [x] + self.popQueue

    def pop(self) -> int:
        self.insertQueue.pop()
        x = self.popQueue.pop(0)
        return x

    def top(self) -> int:
        return self.insertQueue[-1]


    def empty(self) -> bool:
        try:
            return self.insertQueue[0] != self.insertQueue[0]
        except:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()