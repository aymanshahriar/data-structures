# we will need to go back and forth within the linked list, so use a double linked list
class ListNode:
    def __init__(self, val: str, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_node = ListNode(homepage)

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        new_node.prev = self.current_node
        self.current_node.next = new_node
        self.current_node = new_node  # or self.current_node = self.current_node.next

    def back(self, steps: int) -> str:
        count = 1
        while self.current_node.prev != None and count <= steps:
            self.current_node = self.current_node.prev
            count += 1
        return self.current_node.val

    def forward(self, steps: int) -> str:
        count = 1
        while self.current_node.next != None and count <= steps:
            self.current_node = self.current_node.next
            count += 1

tab = BrowserHistory('LC')
tab.visit("go")
tab.visit("fn")
tab.visit("yt")
tab.back(1)
tab.forward
print