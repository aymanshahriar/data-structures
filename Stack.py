from DynamicArray import DynamicArray


class Stack:
    def __init__(self):
        self.stack = DynamicArray(10)   # we can use our own implementation of a dynamic array or just use []

    def push(self, n: int) -> None:
        self.stack.pushback(n)

    def pop(self, n: int) -> int:
        return self.stack.popback(n)

    def peek(self) -> int:
        return self.stack.get(self.stack.getSize() - 1)
