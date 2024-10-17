class MyQueue:

    def __init__(self):
        self.m_stack = []
        self.n_stack = []

    def push(self, x: int) -> None:
        self.m_stack.append(x)

    def pop(self) -> int:
        if len(self.n_stack) == 0:
            self.change()
        return self.n_stack.pop()

    def peek(self) -> int:
        if len(self.n_stack) == 0:
            self.change()
        print(self.m_stack)
        print(self.n_stack)
        return self.n_stack[-1]

    def empty(self) -> bool:
        return len(self.n_stack) == 0 and len(self.m_stack) == 0

    def change(self) -> None:
        while self.m_stack:
            self.n_stack.append(self.m_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
