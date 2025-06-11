class MinHeap:
    def __init__(self):
        self.heap = [-1]

    def push(self, val: int):
        self.heap.append(val)
        val_index = len(self.heap) - 1

        # Percolate Up
        while val_index > 1:
            parent_index = val_index // 2
            if self.heap[val_index] < self.heap[parent_index]:
                self.heap[val_index] = self.heap[parent_index]
                self.heap[parent_index] = val
                val_index = parent_index
            else:
                break

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        min_val = self.heap[1]
        val = self.heap.pop()
        self.heap[1] = val
        val_index = 1

        # Percolate down / bubble down
        while val_index <= len(self.heap) - 1:
            left_child_val = self.heap[2 * val_index] if 2 * val_index <= len(self.heap) - 1 else val
            right_child_val = self.heap[(2 * val_index) + 1] if (2 * val_index) + 1 <= len(self.heap) - 1 else val

            min_child_val = min(left_child_val, right_child_val)

            # The node either has no children of the child/children are greater than the node
            if val <= min_child_val:
                break

            # The node's left child value is smaller than the node's value, so swap the two
            if min_child_val == left_child_val:
                self.heap[val_index] = self.heap[2 * val_index]
                self.heap[2 * val_index] = val
                val_index = 2 * val_index

            # The node's right child value is smaller than the node's value, so swap the two
            else:
                self.heap[val_index] = self.heap[(2 * val_index) + 1]
                self.heap[(2 * val_index) + 1] = val
                val_index = (2 * val_index) + 1

        return min_val

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]):
        self.heap = [-1] + nums
        start = (len(self.heap) - 1) // 2

        for i in range(start, 0, -1):  # Loop will stop after executing i=1
            self._percolate_down(i)

    def _percolate_down(self, val_index: int):

        val = self.heap[val_index]

        while val_index <= len(self.heap) - 1:
            left_child_val = self.heap[2 * val_index] if 2 * val_index <= len(self.heap) - 1 else val
            right_child_val = self.heap[(2 * val_index) + 1] if (2 * val_index) + 1 <= len(self.heap) - 1 else val

            min_child_val = min(left_child_val, right_child_val)

            # The node either has no children or the child/children are greater than the node
            if val <= min_child_val:
                break

            # The node's left child value is smaller than the node's value, so swap the two
            if min_child_val == left_child_val:
                self.heap[val_index] = self.heap[2 * val_index]
                self.heap[2 * val_index] = val
                val_index = 2 * val_index

            # The node's right child value is smaller than the node's value, so swap the two
            else:
                self.heap[val_index] = self.heap[(2 * val_index) + 1]
                self.heap[(2 * val_index) + 1] = val
                val_index = (2 * val_index) + 1





