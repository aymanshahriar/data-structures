# why don't we have methods to insert and remove an element
# from anywhere in the array?
class DynamicArray:

    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity  # capacity is just len(self.array)
        self.array = [0] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    # ie. insert an element into the end of the array
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    # ie. remove the last element of the array
    def popback(self) -> int:
        element = self.array[self.length - 1]
        self.array[self.length - 1] = 0
        self.length -= 1
        return element

    def resize(self) -> None:
        new_array = [0] * 2 * self.capacity
        for index, value in enumerate(self.array):
            new_array[index] = self.array[index]
        self.array = new_array
        self.capacity *= 2

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity
