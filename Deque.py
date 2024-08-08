from doubly_linked_list.LinkedList import LinkedList


class Deque:

    def __init__(self):
        self.linked_list = LinkedList()
        # Back of the deque = tail
        # Front of the deque = head

    def isEmpty(self) -> bool:
        return self.linked_list.head.next == self.linked_list.tail

    def append(self, value: int) -> None:  # Appends to the "back" of the queue (this is the enqueue operation).
        self.linked_list.insert_tail(value)

    def appendleft(self, value: int) -> None:  # Appends to the "front" of the queue
        self.linked_list.insert_head(value)

    def pop(self) -> int:                       # Removes from the "back" of the queue
        val = self.linked_list.remove_tail()
        return val if val != None else -1

    def popleft(self) -> int:                   # Removes from the "front" of the queue (this is the dequeue operation)
        val = self.linked_list.remove_head()
        return val if val != None else -1
