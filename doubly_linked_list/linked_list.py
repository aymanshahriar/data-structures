# This code has been tested because it was used when implementing the deque in Neetcode
from typing import Optional, List

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        # Initialize the list with dummy nodes at the head and tail, which eliminates the need to consider
        # edge cases when inserting or removing from the head or tail.
        # The self.head and self.tail will always point to the dummy nodes, so they will never be re-assigned.
        # The real head the linked list will be the node that comes after the dummy head and the real tail will be the
        # node that comes before the dummy tail.
        self.head = ListNode(-1, None, None)
        self.tail = ListNode(-1, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_head(self, value) -> None:
        new_node = ListNode(value)
        new_node.prev = self.head
        new_node.next = self.head.next

        # These two statements must be in this order. The first statement cannot come after the second statement
        self.head.next.prev = new_node
        self.head.next = new_node

    def insert_tail(self, value) -> None:
        new_node = ListNode(value)
        new_node.next = self.tail
        new_node.prev = self.tail.prev

        # These two statements must be in this order. The first statement cannot come after the second statement
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def remove_head(self) -> Optional[int]:
        # If list is empty (i.e. there are just the two dummy nodes), then return None
        if self.head.next == self.tail:
            return None

        val = self.head.next.value

        # These two statements must be in this order. The first statement cannot come after the second statement
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

        return val

    def remove_tail(self) -> Optional[int]:
        # If list is empty (i.e. there are just the two dummy nodes), then return None
        if self.head.next == self.tail:
            return None
        val = self.tail.prev.value

        # These two statements must be in this order. The first statement cannot come after the second statement
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

        return val

    def get_values(self) -> List[int]:
        lst = []
        cur_node = self.head.next
        while cur_node != self.tail:
            lst.append(cur_node.value)
            cur_node = cur_node.next
        return lst
