from typing import Optional

# Remember that this implementation of the linked list has a dummy node at the head
from singly_linked_list.LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, val) -> None:
        self.linked_list.insert_tail(val)

    # My singly linked list implementation doesn't seem to have a remove_head method
    # Otherwise dequeue would have simply been this statement: return self.linked_list.remove_head()
    def dequeue(self) -> Optional[int]:
        # If queue is empty, return queue
        if self.linked_list.head == self.linked_list.tail:
            return None

        val = self.linked_list.head.next.value
        self.linked_list.head.next = self.linked_list.head.next.next
        return val
