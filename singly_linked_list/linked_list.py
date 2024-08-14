from typing import List

class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)  # Initialize the list with a dummy node which makes it easier to remove a node
                                  # from the beginning of the list
        self.tail = self.head

    def insert_head(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.next = self.head.next
        self.head.next = new_node

        # If the list was empty, we need to set the tail as well.
        if new_node.next == None:  # same as self.head == self.tail
            self.tail = new_node

    def insert_tail(self, value: int) -> None:
        self.tail.next = ListNode(value)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:  # if the index is out of bounds, return False. Else, return True
        before_node = self.head
        before_index = -1

        while before_node.next != None:
            if before_index == index - 1:
                before_node.next = before_node.next.next
                # If we have deleted the last node, then set the before node as the tail
                if before_node.next == None:
                    self.tail = before_node
                return True
            before_node = before_node.next
            before_index += 1

        return False

    def get(self, index: int) -> int:
        current_node = self.head.next
        current_node_index = 0
        while current_node != None:
            if current_node_index == index:
                return current_node.value
            current_node = current_node.next
            current_node_index += 1
        return -1

    def get_values(self) -> List[int]:
        lst = []
        cur_node = self.head.next
        while cur_node != None:
            lst.append(cur_node.value)
            cur_node = cur_node.next
        return lst

    # This method was not included in Neetcode's implementation of a linked list, but was required for
    # leetcode's implemenation of a linked list
    def add(self, index: int, val: int) -> None:
        before_node = self.head
        before_index = -1
        while before_node.next != None:
            if before_index == index - 1:
                new_node = ListNode(val)
                new_node.next = before_node.next
                before_node.next = new_node
                return
            before_node = before_node.next
            before_index += 1

        # Edge case where index specified equals to the length of the linked list
        # (which means we have to add the node at the end/tail of the linked list)
        if before_index == index - 1:
            new_node = ListNode(val)
            self.tail.next = new_node
            self.tail = self.tail.next
